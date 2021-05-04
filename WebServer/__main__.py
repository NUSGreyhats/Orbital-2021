from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    """The index page for the website"""
    return render_template('index.html')


@app.route('/rxss')
def reflected_xss():
    """Page to showcase Reflected XSS"""
    return render_template('rxss.html')

@app.route('/csrf')
def csrf():
    """Page to showcase CSRF"""
    return render_template('csrf.html')


@app.route('/sxss')
def stored_xss():
    """Page to showcase Stored XSS"""
    return render_template('sxss.html')


@app.route('/sqli')
def sqli():
    """Page to showcase SQL Injection"""
    return render_template('sqli.html')


# Run the website as main
if __name__ == '__main__':
    app.run('localhost', 3000, debug=True)