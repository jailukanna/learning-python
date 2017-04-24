from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  # question - does this have to be 'name' or can I customize this?
app.secret_key = '11eedf4f1743a7ed3b08493917215174'
import random # import the random module

# Used for alert messages, 'myClass' and 'startOver' are HTML Class values whom change depending upon conditional expressions below
myClass = 'hidden' # our alert messages start as hidden
startOver = 'hidden' # our start over button starts as hidden
text = '' # our alert text starts as an empty string

@app.route('/')
def index():
	try:
		session['text']
		session['random']
		session['myClass']
		session['startOver']

	except:
		session['random'] = random.randrange(0, 101)
		session['text'] = text
		session['myClass'] = myClass
		session['startOver'] = startOver

	return render_template("index.html", text=session['text'], myClass=session['myClass'], startOver=session['startOver'])

@app.route('/guess', methods=['POST'])
def userGuess():
	session['guess'] = request.form['guess'] # turns user's guess into a python sessions variable
	try:	
		guess = int(session['guess']) # converts our guess to integer for analysis, if string or non-integer, exception below will catch it
		random = session['random'] # assigns random variable to our randomized number - makes for easier analysis during conditional expressions
		if guess > random: # if guess too high:
			session['myClass'] = 'errorHigh'
			session['text'] = 'Too High!'
		  	return redirect('/')

		elif guess < random: # if guess too low:
			session['myClass'] = 'errorLow'
			session['text'] = 'Too Low!'
		  	return redirect('/')

		if guess == random: # if guess correct
			session['myClass'] = 'correct'
			session['text'] = 'Correct!'
			session['startOver'] = 'startOver'
		  	return redirect('/')

	except ValueError:  # if guess is non-int, string or blank submission
		pass
		session['myClass'] = 'errorNone'
		session['text'] = 'You didn\'t guess anything!'
		session['guess'] = 'None'
	  	return redirect('/')

@app.route('/reset') # for reset button
def numReset():
	session['random'] = random.randrange(0, 101)  # assigns new randomized number
	session['myClass'] = 'hidden' # hides alert messages
	session['guess'] = '' # resets guess console
	session['startOver'] = 'hidden' # hides start over button
	return redirect('/')

app.run(debug=True) # runs server
