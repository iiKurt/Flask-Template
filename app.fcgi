#!/var/www/html/public/venv/bin/python
import sys, pathlib
running = str(pathlib.Path(__file__).parent.absolute())
sys.path.append(running + "/Source/") # lets us import stuff when importing from subdirectory

from flup.server.fcgi import WSGIServer
from Source import app, setup

setup()

if __name__ == '__main__':
    WSGIServer(app).run()
