# -*- coding: utf-8 -*-
# Import dependencies:
from __future__ import unicode_literals
from django.shortcuts import render, redirect # allows us to Render pages and Redirect routes
from models import Course # gives us access to `Course` model

def index(request):
    """
    Loads homepage with all courses or creates new 'Course'.

    Note: If 'GET' request, loads homepage with all existing courses. If 'POST'
    request, creates new `Course` and then loads homepage with all courses.
    """

    # If `GET` request, load homepage after getting all `Course`(s).
    if request.method == "GET":
        print "Retrieving all courses and then loading homepage..."
        all_courses = {
            "all_courses": Course.objects.all()
        }
        # Send all courses and load homepage:
        return render(request, "courses/index.html", all_courses)
    # If 'POST' request, validate and create new user:
    elif request.method == "POST":
        print "Validating user now..."
        # Insert validation methods here (using `models.Manager` in your models)
        print "Creating new course...."
        new_course = Course(name=request.POST['name'], description=request.POST['description'])
        new_course.save() # save newly created `Course`
        # Retrieve all courses and load homepage:
        all_courses = {
            "all_courses": Course.objects.all()
        }
        # Send all courses and load homepage:
        return render(request, "courses/index.html", all_courses)

def destroy(request, id):
    """Loads page to confirm deletion of `Course`."""

    print "////// ID OF OBJECT ///////"
    print id
    print "///////////////////////////"

    # If "GET" method, load delete confirmation page:
    if request.method == "GET":
        # Retrieve course by `id`:
        found_course = {
            "found_course": Course.objects.get(id=id)
        }
        return render(request, "courses/confirm_delete.html", found_course)
    else:
        # Delete actual `Course` object.
        print "Deleting course now..."
        # Delete Course:
        Course.objects.get(id=id).delete()
        # Reload homepage (via `GET` request): updated Course list should appear.
        return redirect("/")
