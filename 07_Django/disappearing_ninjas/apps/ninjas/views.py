from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'ninjas/index.html')

def ninjas(request):
	return render(request, 'ninjas/ninjas.html')

def ninja_color(request, color):
	data = {
		'orange' : 'michelangelo',
		'red' : 'raphael',
		'blue' : 'leonardo',
		'purple' : 'donatello'
	}
	if color in data:
		my_ninja = {
			'my_ninja' : data[color],
		}
	else:
		my_ninja = {
			'my_ninja' : 'meganfox',
			'message' : 'DOH!'
		}
	return render(request, 'ninjas/ninja.html', my_ninja)
	# notice how the if else statement checks if 'color in data' - this prevents us from having to write 
	# two routes, we can handle both regex patterns in one route