from django.shortcuts import render, redirect
import string # imports sequences of ASCII characters
import random # imports random number generation

# build a method which combines ascii and numbers in a random fashion:
# ABCD...Z01...9
def randomGenerator(size=14, chars=string.ascii_uppercase + string.digits): # this sets chars to be all the alphabet letters and numbers in one big string (14 char long)
	return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def index(request):
	randomWord = randomGenerator()
	try:
		request.session['attempt'] += 1
		print '**' * 50 
		print request.session['attempt']
		print randomWord
		print '**' * 50 
	except KeyError:
		request.session['attempt'] = 1
		print '**' * 50
		print request.session['attempt']
		print '**' * 50 
	return render(request, 'wordgenerator/index.html', {'randomWord':randomWord}) # note the dictionary format by which variables must be passed along

def generate(request):
	if request.method == 'POST':
		print 'Redirecting for next attempt'
		return redirect('/')
	else:
		return redirect('/')


# note: try re-factoring this code in a way that the form button 
# just goes to ('/') & the index method - and get rid of the generate method entirely!