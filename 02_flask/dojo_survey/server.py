from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	your_name = request.form['your_name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('result.html', your_name = your_name, location = location, language = language, comment = comment)

app.run(debug=True) # run our server w/ debug mode
