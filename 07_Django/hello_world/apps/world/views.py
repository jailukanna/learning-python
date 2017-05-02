from django.shortcuts import render

def index(request): # method name must match what's in urls.py
	print "Hello World!"
	return render(request, 'world/index.html')
