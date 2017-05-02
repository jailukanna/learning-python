from django.shortcuts import render

def index(request):
    """Runs when index route is hit and loads index.html page."""

    return render(request, 'portfolio/index.html')

def testimonials(request):
    """Runs when `/testimonials` route is hit and loads testimonials.html page."""

    return render(request, 'portfolio/testimonials.html')
