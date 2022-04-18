from userspace import userspace
from flask import render_template, abort
from flask_login import login_required, current_user
from extensions import db
from models import User

@userspace.route('/user/<username>')
def root(username):
	user = User.query.filter_by(username=username).first()
	if user:
		return render_template("userspace/user.html", user=user)
	else:
		return abort(404)

@userspace.route('/user/<username>', methods=['DELETE'])
def deleteRoot(username):
	if current_user.is_authenticated and current_user.role == "admin":
		user = User.query.filter_by(username=username).delete()
		db.session.commit()
		return username + "deleted."
	else:
		abort(404)
