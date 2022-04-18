#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/Website/")
sys.path.append("/var/www/Website/Website/") # lets us import stuff when importing from subdirectory
sys.path.append("/var/www/Website/Website/app")

from app import app, setup
setup()
