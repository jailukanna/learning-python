from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.
def index(request):
	time = datetime.datetime.now().strftime('%b %d, %Y, %I:%M:%S')
	data = {
		'currentTime' : time,
	}
	return render(request, 'timedisplay/index.html', data)