from auth import auth

from flask_login import login_user, login_required, logout_user, current_user
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import check_password_hash
from flask_wtf import FlaskForm
from flask import render_template, redirect, url_for
from extensions import db
from models import User

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				return redirect(url_for('userspace.dashboard'))

		return '<h1>Invalid username or password</h1>'
		#return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

	return render_template('login.html', form=form)
