#######
# 
# 	Mission:
#
######

	Create a database, server and pages for a user to register and then login. Once they've registered or have logged in, they should be delivered to a success page.

	1. Create Database /DONE
		+ first_name VARCHAR(255) /DONE
		+ last_name	VARCHAR(255) /DONE
		+ email	VARCHAR(255) /DONE
		+ pw_hash VARCHAR(255) /DONE


	2. Create User Registration with following validations
		+ first_name must be letters only, at least 2 characters /DONE
		+ last_name must be letters only, at least 2 characters /DONE
		+ email must be a valid format /DONE
		+ password must be at least 8 characters /DONE
		+ password confirmation field must match password /DONE

	3. Once you've got the validations working
		+ try keeping them logged in using session /DONE
		+ use session variables to accomplish this task /DONE
		+ associate a session variable to a user id /DONE
		+ than we can check if session variable has been set /DONE

	4. Server

		Setup Routes
			+ ('/')	==> index.html				index() 	GET 	/DONE
			+ ('/success') ==> success.html		create() 	POST 	/DONE
			+ ('/login') ==> success.html		login() 	POST	/DONE

		Import
			+ bcrypt /DONE
			+ session /DONE
			+ redirect, render_template, request /DONE
			+ regex /DONE
			+ mysql /DONE

	5. Pages
		+ index.html 	('/') /DONE
		+ success.html 	('/success') /DONE

	6. Forms
		+ registration form with validations /DONE

	7. Features
		+ Bcrypt password encrpytion /DONE
		+ Form validations /DONE 
		+ Flash messaging /DONE
		+ Session /DONE
		+ Regex /DONE

	8. Extra Features (if time)
		+ logout button /DONE
		+ check when user registers if already exists /DONE


#######
#
# 	Notes from Video 
#
#######

	+ use functions to break up your validation
	+ use a list to capture error messages
	+ see 25m mark onward for ways to improve your code


	See if you can add these extra validations:
	
		+ check login fields so a valid email is required
		+ handle empty fields in login and registration sections







