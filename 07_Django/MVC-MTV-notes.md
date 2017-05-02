# MODEL
+ does verifications
+ builds database tables / properties based on our needs
+ In Django, more logic with the DB occurs here than in most other frameworks
    - This being said, the general convention is, "fat models, skinny controllers"
    - Which means: stuff as much logic into your model, instead of your controller, as possible.

# VIEW (what everyone else calls it)/TEMPLATE(what Django calls it)
+ the data that is served for client-end viewing/interaction (often an HTML with dependencies [which are often, images, JS, CSS, etc])
+ makes http requests based on navigation, form submission, etc, etc.

# CONTROLLER(what everyone else calls it)/VIEW(what Django calls the `Controller` for some awful reason)
+ gets the right data based upon the route
+ routes might point to a controller/view(Django), which may interact with the DB to get data and send it back
+ gathers/builds the data that we hand back to the view (returns the http data and queries the database)

See `django-MVC-diagram.jpg` to see how the various django files fit into the MTV/MVC organization.
