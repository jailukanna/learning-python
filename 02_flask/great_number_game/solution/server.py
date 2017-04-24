from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/', methods = ['GET', 'POST'])
def index():
    data = {}    # QUESTION: Because index() runs every time for ('/'), is it true that other data objects would normally be ovewritten, but because this is a dictionary, the stored values are not erased? AKA, if this was data = [], and I was using .insert() to push items, would these values be erased when index() runs? OR, is the dictionary being reset each time, but the conditional statements below only store one value for data['event']?
    try:
        session['number']
    except:
        session['number'] = random.randrange(0, 101)

    try:
        print request.form
        guess = int(request.form['guess'])
        if guess == session['number']:
            data ={'event':'you got it right'}
            data['coloration'] = 'green'
            data['correct'] = 'true'
        elif guess < session['number']:
            data = {'event':'too low'}
            data['coloration'] = 'blue'
        else:
            data = {'event':'too high'}
            data['coloration'] = 'red'
        data['guess']=str(guess)
        print data
    except:
        data = {'event':'make a guess'}
        data['coloration'] = 'white'
        data['guess']='None yet'
        print data

    return render_template('index.html', data = data)

@app.route('/reset', methods = ['GET'])
def reset():
    session['number'] = random.randrange(0, 101)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)