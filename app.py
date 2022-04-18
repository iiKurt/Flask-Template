import sys, pathlib
running = str(pathlib.Path(__file__).parent.absolute())
sys.path.insert(0, running + "/Source/")
sys.path.append(running + "/Source/Website/") # lets us import stuff when importing from subdirectory

from Website import app, setup

app.debug = True
app.env = "development"
setup()
app.run(host='0.0.0.0', port=80, debug=True)
