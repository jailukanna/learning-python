'''
MODEL
-does verifications
-interacts with database


VIEW/TEMPLATE
-sends http requests


CONTROLLER
-returns data to http request
-receives data from model
'''


# In Django, we define our routes often in a file called 'routes.py' or 'urls.py'
# here's an example of how routes point to our view.py file (which then [i believe] delivers the template)

# This code lives in a urls.py file in your app
from django.conf.urls import url
from . import views
# this urlpatterns list is the key, and Django uses regular expressions to match routes!
# r'^$' -- is the equivalent of '/'. Django is smart and knows that all routes need '/'
urlpatterns = [
    url(r'^$', views.index),
    # So our root route ('/') is directing our app to a method called index in our views.py files...
]

'''
Much like in Flask, the pages that are going to be rendered are found in the templates folder. In general, and as weird as this sounds, we actually put a secondary folder inside the templates folder with the name of our app! Putting our pages that get rendered inside a secondary folder helps us organize our code as we use/build more and more apps. (We’ll do this after we master making a single app, using an MVC strategy).

So far you’ve caught a glimpse of how Django separates routing from the controller method that should run. In an MVC (or, to use Django parlance, an MTV) structure, controller methods generally:

Redirect to other routes
Render specific templates
Invoke methods attached to other pieces of our app that we characterize as models
Models will feel the most foreign, so we are going to talk about them a bit later.
'''



'''




'''