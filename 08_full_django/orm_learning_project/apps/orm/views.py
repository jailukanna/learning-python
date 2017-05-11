from django.shortcuts import render, redirect
from .models import Blog, Comment # this imports our models and allows us to do our orm queries below

# Create your views here.
# skinny views fat controller

def index(request):
	context = {
		'blogs' : Blog.objects.all() # SELECT * FROM blog and gives us all the goods
	}
	print Blog.objects.get(id=1).title
	blog_list = Blog.objects.raw("SELECT * FROM orm_blog;")
	for blogs in blog_list:
		print blogs.title
	return render(request, 'orm/index.html', context) # passing in context lets us now have access to all of our blogs

def blogs(request):
	# using ORM
	print request.POST['title'], request.POST['blog']
	Blog.objects.create(title=request.POST['title'], blog=request.POST['blog']) # this will grab the form elements and save them as 'title' and 'blog'
	# said: insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
	print Blog.objects.all()
	return redirect('/')

def comments(request, id): # make sure when passing id it matches the parameter in your urls.py
	blog = Blog.objects.get(id=id)
	Comment.objects.create(blog=blog, comment=request.POST['comment'])
	return redirect('/')
