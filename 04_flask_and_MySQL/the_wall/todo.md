////////
//
//	The Wall Coding Dojo Assignment
//
////////

	Overview:
		Create a project in which users can register, login, and post messages onto a wall. Other users may comment on posts. All posta and comments should appear most recent to least recent. Once the user has logged in, the user should be directed to the wall. 

	Bonus Points:
		+ Allow a user to delete their own message.
		+ Allow the user to delete his or her message only if it was made in the last 30 minutes.


1. Create Database
	+ users, posts, comments tables...[DONE] 
	+ create columns as shown in wireframe...[DONE] 

2. Create Files:
	+ server.py...[DONE] 
	+ mysqlconnection.py...[DONE] 
	+ templates/index.html...[DONE]
	+ templates/wall.html...[DONE]
	+ static/css/style.css...[DONE] 

3. Create Server Routes and Methods:
	+ ('/') 			('GET')			=>	('index.html') ...[DONE]
	+ ('/register')		('POST')		=>	('wall.html') ...[DONE]
	+ ('/login')		('POST')		=>	('wall.html') ...[DONE]	
	+ ('/post')			('POST')		=>	('wall.html') ...[DONE]
	+ ('/comment')		('POST')		=>	('wall.html') ...[DONE]
	+ ('/edit')			('GET','POST?') =>  ('wall.html') ...[DONE]
	+ ('/delete')		('GET')			=>	('wall.html') ...[DONE]
	+ ('/logout')		('GET')			=>	('index.html') ...[DONE]

4. /templates/index.html:
	+ build registration form...[DONE]
	+ build login form...[DONE]

5. server.py
	+ build registration form validation...[DONE]
	+ build login form validation and password check...[DONE]
	+ add flash messaging and error alerts...[DONE]
	+ add sessions and auto-login after registration/keep on wall if logged in...[DONE]

6. /templates/wall.html
	+ build post form...[DONE]
	+ add post functionality...[DONE]
	+ add list of all messages functionality...[DONE]
	+ add comments functionality...[DONE]
	+ list comments from oldest to newest...[DONE]
	+ add show comments functionality...[DONE]
	+ filter comments display to match corresponding message...[DONE]

7. /static/css/style.css
	+ add styles throughout site...[DONE]
	+ beautify and add a nice background image or texture...[DONE]
	+ could add jQuery UI for practice and to use on buttons...[DONE]


////////
//
//	BONUS Features
//
////////
	+ BONUS: allow user to delete their own message...[DONE]
	+ BONUS: allow user to edit their message within a certain timeframe (30 minutes)...[DONE]


////////
//
//	Current Bugs
//
////////

	+ [RESOLVED]Comments <textarea> name dynamic issue:
		`request.form` was able to grab the dynamic variables by (a) grabbing the entire form and setting this to a variable, `form = request.form`. A dictionary is returned, so in order to access the `comment {{ message['id'] }}` I used the code, `{ 'comment' : form['comment' + id] }`, which gave me the correct field.

	+ [RESOLVED] Comments Validation issue:
		Once this issue was resolved, I was able to build in the validation into the `/comment/<id>`
