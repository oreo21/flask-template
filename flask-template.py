from flask import Flask

app = Flask(__name__)

@app.route("/")
def stdPrint():
	return "Welcome to the main page!"

@app.route("/red")
def printRed():
	return "You are on the <i>red</i> page."

@app.route("/blue")
def printBlue():
	return "You are on the <i>blue</i> page."

@app.route("/yellow")
def printYellow():
	return "You are on the <i>yellow</i> page."

if __name__== '__main__':
	app.run()
