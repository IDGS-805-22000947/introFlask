from flask import Flask

app =Flask(__name__)

@app.route("/")
def index():
	return "Hello,  World!"

@app.route("/Hola")
def hola():
		return "Hola Mundo!"

if __name__ == "__main__":
	app.run(debug=True, port=3000)
