# FlaskSite
A somewhat simple Flask website template. Includes signup/login/logout functionality, CSRF support + a cool folder layout.
Uses my [Kurts-BS](https://github.com/iiKurt/Kurts-BS) template for dark mode (and gradient!) support.

## About
The site itself allows users to register, login, and takes them to their own user profile page.

An admin dashboard is also available that allows the viewing of all table contents and the management of users.

## Setup
To set up the project for the first time, you'll need to create a virtual environment in the root folder:
```
python3 -m venv venv
```

Activate the virtual environment (so we can use `pip` in the context of our virtual environment):
```
source venv/bin/activate
```

Then install the required packages:
```
pip3 install -r "Resources/Requirements.txt"
```

Deactivate the virtual environment, as we're done:
```
deactivate
```

## Note
The database that I've set up has a few extra tables for a different project I'm working on. Ignore it if you like :)

You may want to use bcrypt instead of the SHA256 hash I've set up. (I'll likely push a fix for this in the future)

app.fcgi, some files in the Deploy folder, and the production database connection also reference a different project I'm working on. You'll see references to /var/www/html/public as I store my files under there during production.

Some features such as the admin dashboard, and server configuration, were made for a different project too. Feel free to delete those extra files if you don't need them.
