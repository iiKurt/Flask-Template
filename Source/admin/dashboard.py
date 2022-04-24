from admin import admin

from flask import render_template, abort
from flask_login import current_user
from models import User, Profile, Post, Comment

@admin.route('/dashboard')
def dashboard():
	users = User.query.order_by(User.id)
	profiles = Profile.query.order_by(Profile.id)
	posts = Post.query.order_by(Post.id)
	comments = Comment.query.order_by(Comment.id)
	return render_template("admin/dashboard.html",
		users = users,
		profiles = profiles,
		posts = posts,
		comments = comments)
