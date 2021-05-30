# NUS Greyhats Orbital Security Workshop

# Requirements

1. [Python 3](https://www.python.org/downloads/)
1. A browser of your choice with inspect element functionality

# Quick Start Guide

1. Clone the file into you directory
1. Run `pip install -r requirements.txt` to install dependencies
1. Change directory to WebServer
1. Set the `FLASK_DEBUG` environment variable to `1` if debugging (e.g. `export FLASK_DEBUG=1` (Linux) or `$Env:FLASK_DEBUG = 1` (Powershell))
1. Run `python3 __main__.py`
1. The webserver should be running and if you go to [`http://localhost:3000`](http://localhost:3000) you should be able to see the main page of the website.

# Goals of the workshop

Showcase vulnerabilites:

- SQLI (SQL Injection)
- CSRF (Cross Site Request Forgery)
- Stored XSS (Stored Cross Site Scripting)
- Reflected XSS (Reflected Cross Site Scripting)

# Objectives for workshop

- Explain Website Basics
- Explain CSRF, XSS and SQLi
- Hands on fake orbital website exploit
- Other discussions
- Ads for NUS Greyhats

Link to Workshop Slides: [TBD]()

# Extra challenges

Can you figure out how to do the XSS-CSRF chain while the website has a CSRF Token?
(Answer is in one of the useful links below)

# Tech Stack

1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)

# Other useful links

### XSS

1. [XSS by PortSwigger](https://portswigger.net/web-security/cross-site-scripting)
1. [XSS by OWASP](https://owasp.org/www-community/attacks/xss/)

### CSRF

1. [CSRF by PortSwigger](https://portswigger.net/web-security/csrf)
1. [CSRF by OWASP](https://owasp.org/www-community/attacks/csrf)

### SQLi

1. [SQLi by PortSwigger](https://portswigger.net/web-security/sql-injection)
1. [SQLi by OWASP](https://owasp.org/www-community/attacks/SQL_Injection)

### XSS CSRF Chaining

1. [XSS CSRF Chaining](https://www.doyler.net/security-not-included/xss-attack-chain)

### Other Vulnerabilities not covered in this workshop

1. [Local File Inclusion](https://www.offensive-security.com/metasploit-unleashed/file-inclusion-vulnerabilities)
1. [Template injection](https://portswigger.net/research/server-side-template-injection)

### Other Vulnerable Web App

1. [DVWA](https://dvwa.co.uk/)
1. [OWASP Top 10](https://application.security/free/owasp-top-10)


# Note
Visit our Official Webpage at [NUS Greyhats](https://nusgreyhats.org/)

If you are a student who is interested in helping out with such activities, do contact us [here](mailto:contact@nusgreyhats.org)

If you are a speaker who is willing to present at our security Wednesdays please contact us [here]()