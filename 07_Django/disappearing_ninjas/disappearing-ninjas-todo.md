Disappearing Ninjas Assignment, September 2016, Coding Dojo.

Summary: Create a django project which makes use of routes and route parameters to display different characters based upon their route:


[DONE] + Setup Django Project
	[DONE]+ Call the project disappearing_ninjas, call the app 'ninjas'
	[DONE]+ Create static folders and template folders
	[DONE]+ Create empty index.html file
	[DONE]+ Setup URLS.py files
	[DONE]+ Setup first route in controller

[DONE] + Edit Index.html
	[DONE] + should display, "No Ninjas Here"

[DONE] + Setup '/' index route:
	[DONE] + define in urls.py
	[DONE] + create method in controller

[DONE] + Download images of ninja turtles and save to static/images

[DONE] + Setup '/ninjas' route:
	[DONE] + should display all ninjas
	[DONE] + do you want to have this return a new html page with the image? yes, I ended up making ninjas.html


[DONE] + Setup route parameters so '/ninja/<color>' displays the appropriate ninja:
	[DONE]+ /ninjas/orange -> Michelangelo
	[DONE]+ /ninjas/red -> Raphael
	[DONE]+ /ninjas/blue -> Leonardo
	[DONE]+ /ninjas/purple -> Donatello
	[DONE]+ /ninjas/<anythingelse> -> Megan Fox
	[DONE]+ all of the ninjas/[ninja_color] paths should just be one route (not 5 separate routes…)


Current time: 0:00
Time after deploying Django: 9 minutes 54 seconds
Time Completed: 3 hours 54 minutes
Time Completed + 10:00 for Write-Out: 4 hours and 4 minutes

Why did it take so long, what tripped you up?

+ Named Groups (regex url parameters) 
	+ REGEX patterns -- spent 1+ hour (maybe 2) trying to understand how to properly use my patterns
	+ Started off with the wrong intention of how to use my regex pattern that catched all non-color words

+ Understand now that if we use a catch all regex pattern, this won't override any patterns we've already defined routes for
	+ (ie, if define a pattern for a color word, a catch all will not overwrite it - the color word will be recognized)

+ Context Variables: Make sure to scope the if/else statement in used to render each ninja color -- you'll see the 'if color in data' line, which checks if the color parameter entered in the url exists as a key for the data dictionary. If so, it renders that ninja, otherwise, it defaults to megan fox. This let's you handle both types of patterns in one route. 