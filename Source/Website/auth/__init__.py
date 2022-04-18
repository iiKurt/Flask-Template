from flask import redirect, url_for, Blueprint
from flask_login import LoginManager, login_required, logout_user
from models import User, Profile

auth = Blueprint("auth", __name__,
	template_folder = "templates",
	static_folder = "static",
	static_url_path = "auth/static")

from Website import app
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home.root'))
