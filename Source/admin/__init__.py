from flask import Blueprint, abort
from functools import wraps
from flask_login import current_user

admin = Blueprint("admin", __name__,
	template_folder = "templates",
	static_folder = "static")

# TODO: role_required but take argument defining what role
def admin_role_required(method):
	@wraps(method)

	def check_admin_role(*args, **kwargs):
		if not current_user.is_authenticated or not current_user.role == "admin":
			abort(404)
		else:
			return method(*args, **kwargs)

	return check_admin_role

@admin.before_request
@admin_role_required
def before_request():
	return
