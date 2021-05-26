# NUS Greyhats Orbital Security Workshop


# Requirements
1. [python3](https://www.python.org/downloads/)
1. A browser of your choice

# Quick Start Guide
1. Clone the file into you directory
1. Run `pip install -r requirements.txt` to install dependencies
1. Change directory to WebServer
1. Set the `FLASK_DEBUG` environment variable to `1` if debugging (e.g. `export FLASK_DEBUG=1` (Linux) or `$Env:FLASK_DEBUG = 1` (Powershell))
1. Run `python3 app.py`
1. The webserver should be running and if you go to [`http://localhost:3000`](http://localhost:3000) you should be able to see the main page of the website.


# Goals of the workshop
Showcase vulnerabilites:
- SQLI (SQL Injection)
- CSRF (Cross Site Request Forgery)
- Stored XSS (Stored Cross Site Scripting)
- Reflected XSS (Reflected Cross Site Scripting)


# Timeline for workshop
- Explain HTML
- Explain CSRF, XSS and SQLi
- Hands on fake orbital website exploit
- Other discussions
- Ads for NUS Greyhats

Link to Workshop Slides: https://docs.google.com/presentation/d/12Nu-7dxrrnRzQPQlM6vAUpkDPG2eF9J9FoXwvi_KJpg/edit?usp=sharing

# Tech Stack
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)


# Other useful links
1. [XSS by PortSwigger](https://portswigger.net/web-security/cross-site-scripting)
1. [SQLi by PortSwigger](https://portswigger.net/web-security/sql-injection)
1. [XSS by OWASP](https://owasp.org/www-community/attacks/xss/)
1. [SQLi by OWASP](https://owasp.org/www-community/attacks/SQL_Injection)