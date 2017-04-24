from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')  # route for /root
def index():
	return render_template("index.html", name="Ninja") # index.html

@app.route('/ninjas') # route for /ninjas address
def ninjas():
	return render_template("ninjas.html") # ninjas.html

@app.route('/dojos/new')
def dojos():
	return render_template("dojos.html") # dojos.html

app.run(debug=True)