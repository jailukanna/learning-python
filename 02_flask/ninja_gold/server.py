from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  # question - does this have to be 'name' or can I customize this?
app.secret_key = 'e97e9e5cd77753e2910a7028c0294daf' # needed for sessions
import random # import the random module
import datetime # imports datetime stamp

activity = ['Log now running...']
gold = 0

@app.route('/', methods=['GET','POST'])
def index():
	try:
		session['activity']
		session['gold']

	except:
		session['activity'] = activity
		session['gold'] = gold


	return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def money():
	if request.form['building'] == 'farm':
		session['random'] = random.randrange(10, 21)
		session['gold'] +=  session['random']
		session['now'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
	 	session['activity'].insert(0, 'Worked on the farm and earned ' + str(session['random']) + ' gold! (' + str(session['now']) + ')')
		return redirect('/')

	elif request.form['building'] == 'cave':
		session['random'] = random.randrange(5, 11)
		session['gold'] +=  session['random']
		session['now'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
	 	session['activity'].insert(0, 'Explored a cave and found ' + str(session['random']) + ' gold! (' + str(session['now']) + ')')
		return redirect('/')

	if request.form['building'] == 'house':
		session['random'] = random.randrange(2, 6)
		session['gold'] +=  session['random']
		session['now'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
	 	session['activity'].insert(0, 'Went into the house and found ' + str(session['random']) + ' gold! (' + str(session['now']) + ')')
		return redirect('/')

	elif request.form['building'] == 'casino':
		session['random'] = random.randrange(0, 51)
		session['winOrLose'] = random.randrange(1,3)

		if session['winOrLose'] == 1:
			session['gold'] +=  session['random']
			session['now'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
		 	session['activity'].insert(0, 'Yay! You placed your bets and Won ' + str(session['random']) + ' gold! (' + str(session['now']) + ')')
			return redirect('/')

		else:
			session['gold'] -=  session['random']
			session['now'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
		 	session['activity'].insert(0, 'Oh No! You gambled and lost ' + str(session['random']) + ' gold! (' + str(session['now']) + ')')
			return redirect('/')




app.run(debug=True) # runs server

