from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
	# checks if gold or activity log exist yet
	try: 
		request.session['activity']
		request.session['total_gold']
	# if not start empty log and set gold to 0
	except KeyError:
		request.session['activity'] = ['Activity log now running...']
		request.session['total_gold'] = 0
		print request.session['activity']
		print request.session['total_gold']
	# returns data to be used template side,
	# note: you can also directly reference session on template but 
	# wanted to do it this way to practice context dictionaries
	data = {
		'gold' : request.session['total_gold'],
		'activity' : request.session['activity']
	}
	
	return render(request, 'gold/index.html', data)

def process_money(request):
	if request.method == 'POST':

		# farm
		if request.POST['building'] == 'farm':
			# generate randomized gold between 10-20
			gold_result = random.SystemRandom().randrange(10, 21)
			# add new gold to total gold
			request.session['total_gold'] += gold_result
			# save the current time (and convert it to a string format)
			time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
			# add to activity log: message, gold earned, the time
			request.session['activity'].insert(0, 'Earned ' + str(gold_result) + ' working on the farm... ' + time)
			print '%'*100
			print gold_result
			print request.session['total_gold']
			print time
			print request.session['activity']
			print '%'*100

		# cave
		if request.POST['building'] == 'cave':
			gold_result = random.SystemRandom().randrange(5, 11)
			request.session['total_gold'] += gold_result
			time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
			request.session['activity'].insert(0, 'Earned ' + str(gold_result) + ' from exploring the cave... ' + time)
			print '%'*100
			print gold_result
			print request.session['total_gold']
			print time
			print request.session['activity']
			print '%'*100

		# house
		if request.POST['building'] == 'house':
			gold_result = random.SystemRandom().randrange(2, 6)
			request.session['total_gold'] += gold_result
			time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
			request.session['activity'].insert(0, 'Earned ' + str(gold_result) + ' from inside the house... ' + time)
			print '%'*100
			print gold_result
			print request.session['total_gold']
			print time
			print request.session['activity']
			print '%'*100

		# casino
		if request.POST['building'] == 'casino':
			gold_result = random.SystemRandom().randrange(0, 51)
			place_your_bets = random.SystemRandom().randrange(1, 101)  # generates a number 1 or 100
			time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
			if place_your_bets > 50:
				request.session['total_gold'] += gold_result
				request.session['activity'].insert(0, 'Won ' + str(gold_result) + ' gambling in casino... ' + time)
			else:
				request.session['total_gold'] -= gold_result
				request.session['activity'].insert(0, 'Lost ' + str(gold_result) + ' gambling in the casino... ' + time)
			print '%'*100
			print gold_result
			print request.session['total_gold']
			print time
			print request.session['activity']
			print '%'*100

		return redirect('/')

	else:
		return redirect('/')

