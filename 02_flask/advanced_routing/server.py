# Setup our dependencies:
from flask import Flask, render_template, request, redirect
# Define our Flask application:
app = Flask(__name__)

# Setup our routing:
# Notice the `<username>` variable below which we can use to capture route parameters:
# Just use the `<foobar>` styling for whatever you wish to capture
@app.route('/users/<username>')
def show_user_profile(username):
    print "This is the route parameter:", username
    return render_template("user.html", username=username)
app.run(debug=True)
