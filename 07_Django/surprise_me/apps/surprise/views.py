# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from random import shuffle # imports `shuffle` module

# Setup list of strings that will serve as surprise:
surprises = ["Western Red Cedar", "Douglas Fir", "Noble Fir", "Western Hemlock", "Yellow Cedar", "Subalpine Fir", "Western Red Alder", "Salmon Berry", "Stinging Nettle", "Salaal", "Oregon Grape", "Devil's Club", "English Ivy", "Madrona", "Gary Oak"]

def index(request):
    """Loads index page."""

    return render(request, "surprise/index.html")

def get_surprise(request):
    """Shuffles strings in list and loads results page."""

    new_list = [] # Empty list to hold strings to be added based on user input.
    print "User Guess: {}".format(request.POST["guess"])
    print len(surprises)
    if int(request.POST['guess']) < len(surprises):
        # Shuffle items in the list:
        shuffle(surprises)
        # Add strings from `surprises` list above based on the user integer input:
        for value in range(0,int(request.POST["guess"])): # iterates from 0 - user entered value
            new_list.append(surprises[value]) # adds idx value to list
        results = {
            "surprises": new_list
        }
        print results["surprises"]
        return render(request, "surprise/results.html", results)
    else:
        print "Your guess is too high."
        return redirect("/")
