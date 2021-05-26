FLASK_KEY = 'MYSECRETKEY'

initial_users = [('admin', 'passwordthatissupersecret'), ('user1', 'justaplebuserlmao')]

initial_notes = [
    ('Administration Note', 'Please do not try to hack us, we are proven to be super secure!', 'admin', False),
    ('Dammit', 'We might get hacked and get our secret key exposed, which is SUPERSECRETKEY1012', 'admin', True),
    ('Wow', 'This app looks so fun! I wonder if there is any secrets lying within...', 'user1', False),
]