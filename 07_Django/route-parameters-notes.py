'''
How do we pass along a route parameter? Say we want to pass along /notes/1 for example, how do we do this?

In URLS.py, you would setup your route parameters as follows:

'''

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/(?P<id>this is where your regex pattern goes)$', views.show), 
	url(r'^users/(?P<id>\d+)$', views.show),  # notice '?P' means 'parameter', '<id>' is the parameter, and 'd+' is regex for any number of these parameters (can be many numbers), '$' is the end, ie '/users/123123123' would all catch based on this pattern
	url(r'^/en/(?P<djangoversion>[0-9]\.[0-9])/topics/http/urls/)$', views.index), # note that this will only allow the numbers 0-9
	url(r'^/users/(?P<user_name>\b(john)|(tim)\b)$', views.index), # would search for users/john or users/tim
]



'''
In your VIEWS.py file you would utilize this parameter as follows:

'''

def show(request, id):  # note that <id> param above only requires inner reference, 'id' to be valid
	context = {
		'id': id
	}
	return render_template(request, 'second_app/index.html', context)


'''
in second_app/index.html you could write:

<!-- html -->

<h1> My id is {{id}} </h1>

<!-- end html -->




'''

