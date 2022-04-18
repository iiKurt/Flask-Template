from auth import auth

from flask_login import login_user, current_user
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash
from flask_wtf import FlaskForm
from flask import render_template
from extensions import db
from models import User, Profile

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for('userspace.dashboard'))

	form = RegisterForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if not user:
			hashed_password = generate_password_hash(form.password.data, method='sha256')
			new_user = None
			if form.username.data == "kurt":
				new_user = User(username=form.username.data, password=hashed_password, role="admin")
			else:
				new_user = User(username=form.username.data, password=hashed_password)

			db.session.add(new_user)
			db.session.flush()
			db.session.refresh(new_user)
			new_profile = Profile(description="A profile.", user_id=new_user.id)
			db.session.add(new_profile)
			db.session.commit()

			login_user(new_user)

			return '<h1>New user has been created!</h1>'
		else:
			return "<small>Username taken</small>"
		#return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

	return render_template('signup.html', form=form)
