Ninja Gold, Django Assignment, September 2016, Tim Knab

Summary: Create a web app which allows a ninja to earn gold and display past activities. 

Important Notes:
	+ Your ninja starts with 0 gold
	+ Can go to different places: Farm, Cave, House, Casino and earn different amounts
	+ Casino wages +- 50 gold. 
	+ Create 4 forms on the index route (Farm, Cave, House, Casino)
	+ Form contains hidden input (for now) with a value='' field - this is where you ought to store your building name
	+ Each form submits to /process_money in your views.py, and this is where you'll have to do some logic
	+ Log should exist at bottom of page -- use SESSION to store your ninja gold results/history


[DONE] Setup Django Project: (terminal)
	[DONE] + Create project 'ninja_gold' and app 'gold'
	[DONE] + Create blank urls.py in app/gold
	[DONE] + Create /templates/gold folders (both)
	[DONE] + Create /static/gold/css folders (three)
	[DONE] + Create blank index.html
	[DONE] + Configure urls.py in /ninja_gold (sublime)
	[DONE] + Setup index route and index method to deliver index.html at '/' (sublime)


[DONE] Edit index.html: (templates/gold/index.html)
	[DONE] + Top of page: 'Your Gold': Set a place holder of 0
	[DONE] + Create 4 forms (you may have to inline-block each form - ideally should be a 4 column) (static/gold/css)
	[DONE] + make sure to include csrf token!
	[DONE] + Include an input=hidden whose value=building_name (you'll use this to tell via form submission which gold to award)
	[DONE] + Include an input=submit whose action=/process_money
	[DONE] + Build 'Activities' log textarea - fill with placeholder text


[DONE] Create /process_money route: (views.py)
	[DONE] + build logic to evaluate which form value was submitted
	[DONE] + have each value award separate gold
	[DONE] + in the case of the casino, import random and have gold be either awarded or taken
	[DONE] + use session to record the activities history
	[DONE] + use session to record your current gold score count
	[DONE] + pass this session information to your template
	[DONE] + make sure activities log also captures time stamp (use datetime)


[DONE] Create template variables: (templates/gold/index.html)
	[DONE] + edit index.html so that current gold score and activities log is functional


-------------
Time taken to write this script above: 17 minutes (oof)
Time taken to install django: 6 minutes (boom-shocka-lockah)
Total time to complete project after upload: 2 hours 20 min (not the best, could have done better)
-------------

What tripped you up?
	+ had to remind myself how to initialize session variables before we reference them (try/except - "ask forgiveness not permission")
	+ had to lookup csrf token
	+ had to lookup how to import static css file
	+ styling: remember: to center a group of divs, make sure the wrapper is text-align: center and make sure the inner divs are display: inner-block
		+ styling crude but wanted to center
	+ django-style for loop, had to lookup:
		{% for x in thing %}
			{{x}}
		{% endfor %}

Bonus - Remove the hidden inputs and add a route parameter do this when you have time to learn more):
	+ your strategy would be that each button would submit to something like '/cave'
	+ you would setup 1 route in your urls.py with a regex pattern for '/<building>'
	+ you would then setup a method in your controller so that <building> was evaluated for type of building, and the appropriate gold/message was returned


