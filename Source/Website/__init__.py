from flask import Flask

app = Flask(__name__, 
			template_folder='templates',
			static_folder='static/serve',
			static_url_path='/static')

if __name__ == '__main__':
	app.run(debug=True)

def setup():
	if app.debug:
		app.config['TRAP_BAD_REQUEST_ERRORS'] = True
	app.url_map.strict_slashes = False
	app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	from auth import auth, signup, login
	app.register_blueprint(auth, url_prefix="/")

	from home import home
	app.register_blueprint(home, url_prefix="/")

	from userspace import userspace, user
	app.register_blueprint(userspace, url_prefix="/")

	from admin import admin, dashboard
	app.register_blueprint(admin, url_prefix="/admin")

	register_extensions(app)

from extensions import db, migrate, csrf

def register_extensions(app):
	db.init_app(app)
	migrate.init_app(app, db)
	csrf.init_app(app)
