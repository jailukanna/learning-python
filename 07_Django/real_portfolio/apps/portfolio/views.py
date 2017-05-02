from django.shortcuts import render

def index(request):
    """Loads index page."""

    print "Index route running."
    return render(request, "portfolio/index.html")

def projects(request):
    """Loads projects page."""

    print "Projects route running."
    return render(request, "portfolio/projects.html")

def about(request):
    """Loads about me page."""

    print "About route running."
    return render(request, "portfolio/about.html")

def testimonials(request):
    """Loads testimonials page."""

    print "Testimonials route running."
    return render(request, "portfolio/testimonials.html")
