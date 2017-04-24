from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')  # defines what is served at our root
def index():
	return render_template("index.html", phrase="Hello", times=5)
app.run(debug=True)