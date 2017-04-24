# Setup our dependencies:
from flask import Flask, render_template, request, redirect

# Define our Flask application:
app = Flask(__name__)

# Setup a Ninja Dictionary with Ninja Names and Colors for use in Routing:
ninjas = {
    "blue" : "leonardo",
    "orange" : "michelangelo",
    "red" : "raphael",
    "purple" : "donatello",
}

# Setup our routing:
# Notice the `<foobar>` variable below which we can use to capture route parameters:
# Just use the `<foobar>` styling for whatever you wish to capture

# Index Route (show nothing):
@app.route('/')
def index():
    print "No ninjas here!"
    return render_template("index.html")

# Ninjas Route (show all ninjas):
@app.route('/ninja')
def show_ninjas():
    print "You found all of the ninjas!"
    # Render ninja page but send complete ninja dictionary since we want all ninjas:
    return render_template("ninja.html", ninjas=ninjas)

# Ninja Route (show one ninja or April if not valid color):
@app.route('/ninja/<color>')
def show_ninja(color):
    print "This is the route parameter:", color
    # If the color is either of the Ninja's colors, then load the Ninja Page and appropriate Ninja:
    if (color == 'blue') or (color == 'orange') or (color == 'red') or (color == 'purple'):
        # Load ninja page and send appropriate ninja name from dictionary above:
        return render_template("ninja.html", ninja=ninjas[color])
    # This will only run if the `<color>` route parameter is not a valid ninja color:
    # Render Ninja page but with April:
    return render_template("ninja.html", ninja='notapril')


# Run App in Debug Mode:
app.run(debug=True)
