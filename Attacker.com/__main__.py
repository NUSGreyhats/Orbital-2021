from flask import Flask
from flask.templating import render_template

# Create the application
app = Flask(__name__)


@app.route('/')
def index():
    """Main page of the Webpage"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run('localhost', 3001, debug=True)
