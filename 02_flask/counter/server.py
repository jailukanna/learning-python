from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  # question - does this have to be 'name' or can I customize this?
app.secret_key = 'CounterSecretKey'


@app.route('/')
def index():
	try:
		session['counter']  # QUESTION: what exactly is happening here?
		# Re: You're trying to access the value at the "counter" key of session, but if it doesn't yet exist the program will error out. That's why wrapping it in a "try" block can help, but there's another strategy too: You can just ask "if 'counter' not in session: "
	except:
		session['counter'] = 0
    
	session['counter'] = session['counter'] + 1	
	return render_template("index.html", counter=session['counter'])


@app.route('/increment_2')
def incrementByTwo():
	session['counter'] = session['counter'] + 1
	return redirect('/') 


@app.route('/reset')
def resetCounter():
	session['counter'] = 0
	return redirect('/') 

app.run(debug=True) # run our server w/ debug mode

