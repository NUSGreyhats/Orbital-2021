import os
import sqlite3
from flask import Flask, render_template, redirect, request, flash

# Initialise the application
app = Flask(__name__)
app.secret_key = 'MYSECRETKEY'

# Contants
DB_PATH = os.path.join('data', 'data.db')
REGISTER_QUERY = 'INSERT INTO users VALUES ({}, {})'
BLANK_ERROR_MSG = 'Please do not leave any fields blank!'
CREATE_QUERY = 'CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)'
LOGIN_QUERY = 'SELECT * FROM users WHERE username = \'{}\' AND password = \'{}\''

OTHER_DB_PATH = os.path.join('data', 'data2.db')
CREATE_PLANT_QUERY = 'CREATE TABLE IF NOT EXISTS plants (name TEXT)'
SEARCH_QUERY = 'SELECT * FROM plants p WHERE p.name LIKE \'%\' || ? || \'%\''


# Database methods
def create_db() -> None:
    """Create the database if it does not exist"""
    # Check if database exists
    with sqlite3.connect(DB_PATH) as db:

        # Create the table if it does not exist
        cur = db.cursor()
        cur.execute(CREATE_QUERY)

    with sqlite3.connect(OTHER_DB_PATH) as db:

        # Create the table if it does not exist
        cur = db.cursor()
        cur.execute(CREATE_PLANT_QUERY)


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
    with sqlite3.connect(OTHER_DB_PATH) as db:
        cur = db.cursor()

        # Create the table if not exists
        cur.execute(CREATE_PLANT_QUERY)

        # Search for the plant

        # Use prepared statements here to prevent SQLi
        cur.execute(SEARCH_QUERY, (data['query'],))
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
    with sqlite3.connect(DB_PATH) as db:
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
