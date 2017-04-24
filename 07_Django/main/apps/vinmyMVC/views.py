from django.shortcuts import render, redirect

# This is your controller
# Create your views here.
# always takes 3 variables, 'request, url, dictionary'
def index(request):
	return render(request, 'vinmyMVC/index.html')

def show(request):
	return render(request, 'vinmyMVC/show_users.html')

def create(request):
	print request.method
	# take note of the if / else statement below, in order for django to listen to our posts,
	# we have to make sure that we do an if check for 'POST' or 'GET'
	# second note: if we use request.method == POST, then we ought to use request.POST
	# if we use request.method == GET, then we ought to use request.GET
	if request.method == 'POST':
		# do something
		print '*'*50
		print request.POST
		request.session['name'] = request.POST['first_name']
		print request.session
		print '$'*50
		print request.session['name']
		print '*'*50
		return redirect('/')
	else:
		return redirect('/')