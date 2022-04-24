# FlaskSite
A somewhat simple Flask website template. Includes signup/login/logout functionality, CSRF support + a cool folder layout.
Uses my [Kurts-BS](https://github.com/iiKurt/Kurts-BS) template for dark mode (and gradient!) support.

## About
The site itself allows users to register, login, and takes them to their own user profile page.

An admin dashboard is also available that allows the viewing of all table contents and the management of users.

## Note
The database that I've set up has a few extra tables for a different project I'm working on. Ignore it if you like :)

app.fcgi, some files in the Deploy folder, and the production database connection also reference a different project I'm working on. You'll see references to /var/www/html/public as I store my files under there during production.

Some features such as the admin dashboard, and server configuration, were made for a different project too. Feel free to delete those extra files if you don't need them.
