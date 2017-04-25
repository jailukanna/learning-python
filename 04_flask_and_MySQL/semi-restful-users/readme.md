Optional Assignment: Semi-Restful Users
It's very common for a web application to provide the user interface for the users to create, read/retrieve, update, or destroy a 'resource'.  For example, imagine you want to build a web application that allows the user to create/read/update/destroy users. There are many ways that you can build web applications like this.  For example, you could have resources called users, products, pd (short for products) and so forth.  You could also have different methods that essentially do the same thing.  So, to display user information for user id 1, you could have the URL 'users/1' provide this info or 'users/show/1' or 'users/show_info/1' or 'users/display/1', etc.

Since many web applications essentially do these CRUD (create/retrieve/update/destroy) operations, you can imagine how confusing this could get if everyone followed different ways of creating controllers and methods names to do these operations.

REST or RESTful route is basically a rule developed by someone that outlined some rules for everyone to follow.  It's up to you whether you also follow these rules/conventions but it is strongly encouraged that you get yourself familiar with how RESTful routes work, as a lot of people in the industry are also following these rules.

Right now with Flask, it's not quite possible for you to do the full RESTful architecture, so the exercise below is to help you get somewhat familiar with RESTful routes. Later when you get into other stacks (such as MEAN or Rails), you'll already be somewhat familiar with REST concepts.

Follow the instructions in the wireframe below to build this application in Flask.  



Make sure to...

Have 7 routes in your server.py. Because we are working with 'users', they might look like:

+ a GET request to /users - calls the index method to display all the users. This will need a template. //DONE

+ GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template. //DONE

+ GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template. //DONE

+ GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template. //DONE

+ POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created. //DONE

+ GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted. //DONE

+ POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated. //DONE


## Still To Do:

+ Build Edit Page
+ Add Show Link / Links to User
