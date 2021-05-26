import os
import sqlite3
from flask import Flask, render_template, redirect, request, flash
from util import FLASK_KEY, initial_users, initial_notes

# Initialise the application
app = Flask(__name__)
app.secret_key = FLASK_KEY

# Constants
USERS_DB_PATH = os.path.join('data', 'users.db')
INSERT_USERS_QUERY = 'INSERT INTO users VALUES (?, ?)'
BLANK_ERROR_MSG = 'Please do not leave any fields blank!'
CREATE_USERS_QUERY = 'CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT)'
LOGIN_QUERY = 'SELECT * FROM users WHERE username = \'{}\' AND password = \'{}\''

NOTES_DB_PATH = os.path.join('data', 'notes.db')
CREATE_NOTE_QUERY = 'CREATE TABLE IF NOT EXISTS notes (name TEXT, content TEXT, user TEXT, private TINYINT)'
INSERT_NOTE_QUERY = 'INSERT INTO notes VALUES (?, ?, ?, ?)'
SEARCH_NOTES_QUERY = 'SELECT * FROM notes p WHERE p.name LIKE \'%\' || ? || \'%\''

CHECK_TABLE_EXIST = ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''

# Database methods
def create_db() -> None:
    if not os.path.exists('data'):
        os.makedirs('data')

    """Create the database if it does not exist"""
    # Check if database exists
    with sqlite3.connect(USERS_DB_PATH) as db:
        cur = db.cursor()

        cur.execute(CHECK_TABLE_EXIST.format('users'))
        #if the count is 1, then table exists
        if cur.fetchone()[0] != 1:

            # Create the table
            cur.execute(CREATE_USERS_QUERY)
            # Add initial list of users, e.g. admin, user1
            for (username, password) in initial_users:
                cur.execute(INSERT_USERS_QUERY, (username, password))

    with sqlite3.connect(NOTES_DB_PATH) as db:
        cur = db.cursor()

        cur.execute(CHECK_TABLE_EXIST.format('notes'))
        #if the count is 1, then table exists
        if cur.fetchone()[0] != 1:

            # Create the table
            cur.execute(CREATE_NOTE_QUERY)
            # Add initial list notes
            for (name, desc, user, private) in initial_notes:
                cur.execute(INSERT_NOTE_QUERY, (name, desc, user, private))


@app.route('/')
def index():
    """The index page for the website"""
    return render_template('index.html')


# Reflected XSS Methods
@app.route('/rxss', methods=['POST', 'GET'])
def reflected_xss():
    """Page to showcase Reflected XSS"""
    if request.method == 'GET':
        return render_template('rxss.html')

    # Get form data
    data = request.form

    # Check if input is empty
    if len(data) == 0 or len(data['query'].strip()) == 0:
        flash("Data cannot be empty")
        return render_template('rxss.html')

    # Fetch the data from the database
    with sqlite3.connect(NOTES_DB_PATH) as db:
        cur = db.cursor()

        # Create the table if not exists
        cur.execute(CREATE_NOTE_QUERY)

        # Search for the plant

        # Use prepared statements here to prevent SQLi
        cur.execute(SEARCH_NOTES_QUERY, (data['query'],))
        results = tuple(map(lambda x: x[0], cur.fetchall()))

    return render_template('rxss.html', results=results, query = data['query'])


# CSRF Methods
@app.route('/csrf')
def csrf():
    """Page to showcase CSRF"""
    return render_template('csrf.html')


# Stored XSS Methods
@app.route('/sxss')
def stored_xss():
    """Page to showcase Stored XSS"""
    return render_template('sxss.html')


# SQLi Methods
def parse_args(username: str = None, password: str = None, **kwargs):
    """Parse the arguments from the user"""
    return username, password


@app.route('/sqli', methods=['GET', 'POST'])
def sqli():
    """Page to showcase SQL Injection"""

    # If it is a get request return the webpage
    if request.method == 'GET':
        return render_template('sqli.html')

    # Check if the arguments are valid
    data = request.form
    if data == None:
        flash('There is no data')
        return render_template('sqli.html')

    username, password = parse_args(**data)

    # Check for empty data
    if None in (username, password):
        flash('Please enter a valid username or password')
        return render_template('sqli.html')

    # Check if the entry exists
    with sqlite3.connect(USERS_DB_PATH) as db:
        cursor = db.cursor()
        query = LOGIN_QUERY.format(username, password)
        cursor.execute(query)
        result = cursor.fetchall()

    # If there are no users found
    if len(result) == 0:
        flash('Invalid username or password')
        return render_template('sqli.html')

    # Get the matched user
    user = result[0]

    # Set a cookie
    return render_template('logged_in.html', username=user[0], query=query)


# Run the website as main
if __name__ == '__main__':
    create_db()
    app.run('localhost', 3000, debug=True)
