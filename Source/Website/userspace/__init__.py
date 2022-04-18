from flask import Blueprint

userspace = Blueprint("userspace", __name__,
	template_folder = "templates",
	static_folder = "static",
	static_url_path = "userspace/static")
