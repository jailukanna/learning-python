#############
#
# 	AJAX NOtes Assignment
#
#############

	Summary: Create a note application by which a user enters a title for a not, and upon clicking submit, the note appears, with a new text box beneath it, allowing us to an enter a description. Clicking the box lets us edit it. A delete button appears for each note.


	+ [DONE] Create database with a table called, 'notes':
		+ [DONE] include the following columns: 
			+ id
			+ title
			+ description
			+ created_at
			+ updated_at

	+ [DONE] Create templates/index.html:
		+ [DONE] include page title
		+ [DONE] include form for adding note (1)

	+ [DONE] Create templates/partials/index.html:
		+ [DONE] make sure to only include what's in your loop

	+ [DONE] Create mysqlconnector.py

	+ [DONE] Create server.py and connect to mysqlconnector.py

	+ [DONE] Create your routes:
		+ ('/') - GET - renders index.html
		+ ('/notes/index_json') - GET - renders JSON object
		+ ('/create') - POST - renders redirect to '/' (no ajax yet)
		+ ('/<id>/update/description') - POST - redirect to '/'
		+ ('/<id>/update/title') - POST - redirect to '/'
		+ ('/<id>/delete') - POST - redirect to '/'


	+ [DONE] Build this first without AJAX

	+ [DONE] Add in AJAX and update routes
