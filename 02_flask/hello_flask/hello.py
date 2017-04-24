from flask import Flask, render_template	# Import Flask to allow us to create our app. ** render_template allows us to render our html pages **
app = Flask(__name__)		# Global variable __name__ tells Flask whether or not we are running the file.

@app.route('/')  			# '@'symbol designates a 'decorator' which attaches the followingL ('/') in the route function tells the computer when a request to localhost:5000 is made, we run "hello_world".
def hello_world():			
	return "Hello World!"

@app.route('/success')
def success():
	return render_template('success.html', name='Tim')

app.run(debug=True)			# Turns on debug mode -- note this ** MUST ** go at the end else your @app.routes won't work!
