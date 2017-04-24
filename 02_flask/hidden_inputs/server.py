from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  # question - does this have to be 'name' or can I customize this?
app.secret_key = '95d8ac53b544781d2e2f4f63567c940d'


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/process', methods=['POST'])  # very important when using hidden fields to make sure you've defined your method (POST)
def myProcess():
	if request.form['action'] == 'register':  # 'register' is the value from our form
		session['registered'] = True
		# do registration process
	elif request.form['action'] == 'login':	# 'login' is the value from our form
		session['login_info'] = True
		# do login process
	return redirect('/') 


app.run(debug=True) # run our server w/ debug mode



# hidden fields can still be accessed via the page source. Other users can see and change values set in hidden input, so be careful if choosing to store very sensitive data (or make sure to protect it if you do)