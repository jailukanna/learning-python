# Templates and Static Files Review
In our views file, Django knows to look in the templates folder first for whatever
path we pass to our render method.

  `# views.py
  ...
  def index(request):
    return render(request, "ourApp/index.html")`

So this code actually tells the index method to look in templates/ourApp and then at the index.html file.

The behavior for static files is very similar: Django’s template rendering system knows (if it's told) to look in the static and then at the path for the specific file relative to that folder!

What this looks like in HTML is:

    `<!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title></title>
        {% load staticfiles %}
      <!-- The line above tells Django to be ready to listen for static files -->
      <link rel="stylesheet" href="{% static 'ourApp/css/main.css' %}"media="screen" title="no title"  charset="utf-8">
      </head>
    <body>
    </body>
    </html>`

In other words, loading static files, whether it's CSS or JavaScript or images, will start the search path inside of ourApp’s static folder, and after that, the rest of that path is up to us! A good habit to get into is separating our JavaScript, CSS, and images into three folders (and specifying which app we are retrieving these files from, as outlined in the structure at the top of this tab!

Note the Django templating call inside the link tag too!
