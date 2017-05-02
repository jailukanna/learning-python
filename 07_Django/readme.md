# Django
Django is a MTV framework for Python that gives us some benefits over Flask-based
applications. Django is useful for applications where you've got a lot going on,
and because Django modularizes components of your app, this allows for cleaner
organization as things scale up. However, even for small applications, the
organization and structure is useful. This modularized format is also how other stacks
operate when using an MVC framework, so understanding the organization enables you
when later taking on other languages or stacks.

## Why Django?
As our projects get larger we can see the benefits of Django as compared to Flask. Django emphasizes the use of individual apps, each of which has its own MTV structure. These separate apps are really features that can be compartmentalized. Building multiple apps and telling them how to talk to each other is an advanced skill you'll find in our extras section. For now just know that it can be useful to break large projects into smaller pieces.

## Separating Concerns
In Flask, we’ve been combining everything into one large (potentially monster) file. Django's MTV structure allows us to outsource the different kinds of tasks to specific file locations. Here's how a single request will pass around data within our app:

## Routes
The first handler for assigning tasks correctly is routing. Routing is handled by a separate document that contains a list of available routes and calls to the appropriate view functions. When a request is received routing identifies the view method to be called.

## The View File
Next, the appropriate views function will be executed. In our MTV structure, view functions generally:

## Redirect to other routes
Render specific templates
Invoke methods attached to other pieces of our app that we characterize as models

## Models
It is likely that the views file will call some model method in order to perform some operation on the database. Models should do the following:

## Build database tables
Handle logic related to database operations, including validation

##Templates
Lastly, a view function will either render a template or redirect. When a template is rendered Django has to parse the file looking for logic or variables you've inserted, interpret those, before sending a complete HTML document as a response to the client. Django templates are so similar to Flask (Jinja2) templates that you'll hardly notice a difference.
