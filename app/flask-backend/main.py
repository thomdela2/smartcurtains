import flask

app = flask.Flask("__main__")

@app.route("/")
def my_index():
	return flask.render_template("index.html", token="React app running on Flask")

app.run(debug=True)