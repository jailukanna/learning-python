# Form Data
As you’ve already seen, getting information from a user via forms is an extremely important part of web development. When we were using Flask, we used the form property of the request object to access input values.

Django behaves very similarly, except the property is `request.POST` (instead of `request.form`).
Use `request.GET` for `GET` requests and `request.POST` for `POST` requests.

## Key Terms
    + request.POST
        - Data from POST request.
    + request.GET
        - Data from GET request.
    + request.method
        - Returns the method/HTTP verb associated with the request.
    + {% csrf_token %}
        - Prevents cross-site request forgery (place it in a form on the HTML/template side of your project).
        - Add this *directly beneath* your `<form>` tag.

Your form might look like this for a POST request:
    `<form action="/new_user" method="POST">
    	{% csrf_token %}
    	<input type="text" name="first_name">
    	<input type="submit" value="submit">
    </form>`

And your route to handle that post might look like this:
    `url(r'^new_user$',views.create)`

And the method in your `views` controller might look like this:
    `from django.shortcuts import render, redirect
    def create(request):
    	if request.method == "POST":
    		print "*"*50
    		print request.POST
    		print request.method
    		print "*"*50
    		return redirect("/")
    	else:
    		return redirect("/")
    `
    - Notice how the `if request.method == "POST":` is used to check the method
    and work accordingly.

# Session Data:
To setup session, make sure you've first *run any migrations* that you may see a warning for from Django when running your server.

Here's how:
    `python manage.py makemigrations`
    `python manage.py migrate`

# Session

Now we can restart our server and use session:

    `request.session` # It's a dictionary, so you can attach key/value pairs
    ie, `request.session['name'] = request.POST["name"]`

Now, let's try out session. In the create function, add the following:

    `request.session['name'] = request.POST['first_name']`

And in `index.html` add the following in a line above your form:

    `{{request.session.name}}`

Useful session methods:
    + `request.session['key']`
        - This will retrieve (get) the value stored in key
    + `request.session['key'] = "value"`
        - Set the value that will be stored by key
    + `del request.session['key']`
        - Deletes a session key if it exists, throws a `keyError` if it doesn’t.
        - Use along with `try` and `except` since it’s *better to ask for forgiveness than permission*
    + `'key' in request.session`
        - Returns a boolean of whether a key is in session or not
    + `{{ request.session.name }}`
        - Use dot notation (.) to access `request.session` keys from templates since square brackets ([]) aren’t allowed there

## Note: Session in Django gets saved even if we leave the browser!
