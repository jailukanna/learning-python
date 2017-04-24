CRUD Operations
		Create /DONE
		Read /DONE
		Update /DONE
		Delete /DONE

	1. create database /DONE
		+ first_name /DONE
		+ last_name /DONE
		+ email /DONE
		+ created_at /DONE
		+ updated_at /DONE

	2. create server
		+ routing
			+ '/'  						(GET) show all friends /DONE
			+ '/friends'				(POST) create a friend /DONE
			+ '/friends/<id>/edit'		(GET) edit a friend /DONE 
			+ '/friends/<id>'			(POST) update a friend /DONE
			+ '/friends/<id>/delete' 	(POST) delete a friend /DONE

	3. front end
		+ 'templates' folder
			+ index.html /DONE
			+ edit.html /DONE
		+ 'static' folder
			+ style.css /DONE

	4. validations and messaging
		+ email validation /DONE
		+ flash messaging /DONE

			+ QUESTION 1: Can we just review the concept of '[0]' for our flask variables?
			+ QUESTION 2: How can I setup different colored alerts with flash messaging?
			+ QUESTION 3: Why is my Flash Messaging on 'edit.html' not working?
			+ QUESTION 4: What is 'filtering' for flash messages? (bonus idea)
			+ EXTRA: regex checks on first and last name (no foreign characaters) 
			+ EXTRA: check if user already exists (no duplicates)