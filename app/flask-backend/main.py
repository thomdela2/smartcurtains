import flask

app = flask.Flask("__main__")

@app.route("/")
def my_index():
	return "Homepage"
	# return flask.render_template(
	# 	"index.html", 
	# 	token="React app running on Flask",
	# 	)

@app.route("/hello")
def hello():
	return "Hellopage"


app.run(debug=True)