import sys, pathlib
running = str(pathlib.Path(__file__).parent.absolute())
sys.path.append(running + "/Source/") # lets us import stuff when importing from subdirectory

from Source import app, setup

if "--debug" in sys.argv:
	print("Running in debug mode...")
	app.debug = True
	app.env = "development"
	setup()
	app.run(host='0.0.0.0', port=80, debug=True)
else:
	print("Not running directly...")
	print("...use \"--debug\" to run in debug mode.")
	setup()
