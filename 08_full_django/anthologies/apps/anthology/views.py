# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    """Loads homepage."""

    # Create 3 New Authors:
    # tim = Author(name="Tim Knab", dob="1984-09-26")
    # tim.save()
    # julianna = Author(name="Julianna Giles", dob="1988-07-02")
    # julianna.save()
    # chris = Author(name="Chris Knab", dob="1987-11-16")
    # chris.save()

    # Create 3 New Anthologies:
    # poems = Anthology(title="A Collection of Poems", publish_date="2001-01-01")
    # poems.save()
    # essays = Anthology(title="Essays On Life", publish_date="2002-01-01")
    # essays.save()
    # shorts = Anthology(title="Short Stories to Laugh With", publish_date="2003-01-01")
    # shorts.save()

    # Add Author to Anthology:
    # tim.anthologies.add(poems)
    # tim.anthologies.add(essays)
    # tim.anthologies.add(shorts)

    # Add More Authors to Anthology:
    # chris.anthologies.add(poems)
    # julianna.anthologies.add(poems)

    # Retrieve all `Authors` for `poems`:
    # poem_authors = poems.author_set.all() # can iterate over this

    # Retreive all anthologies for an Author:
    # tim_anthologies = tim.anthologies.all()

    # Create and add an anthology to a user in one line flat:
    # feels = tim.anthologies.create(title="Feels from the Heart", publish_date="2001-01-01")

    # Now if we print anthologies for tim, the new anthology 'feels from the heart' will show:
    # tim_anthologies = tim.anthologies.all()

    return render(request, "anthology/index.html")
