# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    print "Running index() method..."
    print "Loading index.html..."
    return render(request, "landscape/index.html")

def scene(request, integer):
    print integer
    integer = int(integer)
    if integer >= 1 and integer <= 10:
        # deliver snow image
        image = {
            "url": 'snow'
        }
        return render(request, "landscape/scene.html", image) 
    if integer >= 11 and integer <= 20:
        # deliver desert image
        image = {
            "url": 'desert'
        }
        return render(request, "landscape/scene.html", image)
    if integer >= 21 and integer <= 30:
        # deliver forest
        image = {
            "url": 'forest'
        }
        return render(request, "landscape/scene.html", image)
    if integer >= 31 and integer <= 40:
        # deliver vineyard
        image = {
            "url": 'vineyard'
        }
        return render(request, "landscape/scene.html", image)
    if integer >= 41 and integer <= 50:
        # deliver tropical landscape
        image = {
            "url": 'tropical'
        }
        return render(request, "landscape/scene.html", image)
    else:
        # integer invalid
        print "Integer out of range. Redirecting..."
        return redirect("/")
