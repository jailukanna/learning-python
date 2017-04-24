from flask import Flask, render_template, request, redirect, session    # session import is required if you want to store data as a cookie or session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'   # session import also requires the creation of a unique key

@app.route('/')
def index():
	return render_template("index.html")
	# handles our form submission
	# note that above we defined our HTTP methods

@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	# don't worry about nxt lines till later
	# about forms
	session['name'] = request.form['name']   # notice how the session['variable'] is used to store these variables
	session['email'] = request.form['email']
	# redirect back to '/' route
	return redirect('/show') # using redirect method we imported and we want to redirect to '/show' route


@app.route('/show')
def show_user():
	return render_template('user.html')

app.run(debug=True) # run our server w/ debug mode

