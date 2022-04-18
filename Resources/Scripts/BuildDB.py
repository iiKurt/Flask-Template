"""
use this file like so:
if on dev server:
	python3 BuildDB.py --debug
if on production server:
	python3 BuildDB.py

use the --reset option if you need to wipe the DB (useful when adding new columns)
"""

import sys, pathlib

debug = False
drop = False

# and the worse code award of the century goes to:
if "--debug" in sys.argv:
	debug = True
if "--reset" in sys.argv:
	drop = True

if debug:
	running = str(pathlib.Path(__file__).parent.absolute())
	sys.path.insert(0, running + "/../../Source/")
	sys.path.append(running + "/../../Source/Website/") # lets us import stuff when importing from subdirectory
else:
	sys.path.insert(0, "/var/www/Website/")
	sys.path.append("/var/www/Website/Website/")

from Website import app, register_extensions

register_extensions(app)
app.debug = debug

from Website import *

with app.app_context():
	db.session.commit() # commit any unfinished changes

	if drop:
		print("Dropping all tables...")
		db.drop_all()

	db.create_all()
	db.session.commit()
