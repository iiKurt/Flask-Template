from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from extensions import db
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	password = db.Column(db.String(120))
	join = db.Column(db.DateTime, server_default=func.now(), nullable=False)
	role = db.Column(db.String(15))

class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(256))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
	posts = db.relationship('Post', backref='profile', lazy=True)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False) 
	title = db.Column(db.String(64))
	contents = db.Column(db.String(256))
	posted = db.Column(db.DateTime, server_default=func.now(), nullable=False)
	replies = db.relationship('Comment', backref='post', lazy=True)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False) 
	parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
	replies = db.relationship('Comment', remote_side=[id], backref='comment', lazy=True)
	author_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
	contents = db.Column(db.String(256))
	posted = db.Column(db.DateTime, server_default=func.now(), nullable=False)
