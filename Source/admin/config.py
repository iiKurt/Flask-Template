from admin import admin, admin_role_required
from configuration import config_object

from flask import render_template, request, Response, flash

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from werkzeug.datastructures import ImmutableMultiDict

class ConfigForm(FlaskForm):
	#BooleanField.false_values = {False, 'false', ''}
	# do NOT use name="whatever" as it breaks wtf-json
	accountCreation = BooleanField("Enable Account Creation")
	posting = BooleanField("Enable Posting")


@admin.route('/config', methods=['GET', 'POST'])
def config():
	form = ConfigForm()

	if form.validate_on_submit():
		newConfig = dict(form.data)
		del newConfig['csrf_token']
		config_object.set_config(newConfig)
		flash("Successfully applied changes!", "success")
		return render_template("admin/config.html", form=form)
	
	try:
		form.process(ImmutableMultiDict(config_object.get_config()))
	except ValueError:
		pass

	return render_template("admin/config.html", form=form)
