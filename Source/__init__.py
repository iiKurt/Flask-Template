from flask import Flask

app = Flask(__name__, 
			template_folder='templates',
			static_folder='static/serve',
			static_url_path='/static')

def setup():
	if app.debug:
		app.config['TRAP_BAD_REQUEST_ERRORS'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../devdatabase.db'
		app.config['PROPAGATE_EXCEPTIONS'] = True
		app.config['TESTING'] = True
	else:
		app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://www-data:password@localhost/public_schema'
	app.url_map.strict_slashes = False
	app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	from auth import auth, signup, login
	app.register_blueprint(auth, url_prefix="/")

	from home import home
	app.register_blueprint(home, url_prefix="/")

	from userspace import userspace, user
	app.register_blueprint(userspace, url_prefix="/")

	from admin import admin, dashboard, config
	app.register_blueprint(admin, url_prefix="/admin")

	register_extensions(app)

from extensions import db, migrate, csrf, login_manager

def register_extensions(app):
	login_manager.init_app(app)
	login_manager.login_view = 'auth.login'
	db.init_app(app)
	migrate.init_app(app, db)
	csrf.init_app(app)

if __name__ == '__main__':
	app.run(debug=True)
