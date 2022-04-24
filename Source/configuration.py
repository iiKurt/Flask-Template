from json import load, loads, dump, dumps
from os import path

class ServerConfiguration:
	script_dir = path.dirname(__file__)
	config_file = dumps({})

	def __init__(self):
		try:
			self.config_file = load(open(path.join(self.script_dir, "config.json")))
		except FileNotFoundError:
			# we will just write a new one when setting :)
			pass

	def get_config(self):
		return self.config_file

	def set_config(self, config):
		if config is str:
			self.config_file = loads(config)
		else:
			self.config_file = config
		
		with open(path.join(self.script_dir, 'config.json'), 'w') as conf:
			dump(self.config_file, conf, indent="\t", sort_keys=True)

config_object = ServerConfiguration()
