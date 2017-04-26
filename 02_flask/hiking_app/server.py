#-------------------------#
#----- Project Notes -----#
#-------------------------#
'''
Author: https://github.com/natureminded
Website: http://sasquat.ch
Note: This is just a single page app, without ajax for now.
'''

#----------------------------------------------#
#----- Setup Application AND Dependencies -----#
#----------------------------------------------#
from flask import Flask, request, redirect, render_template, session, flash # project dependencies
import hiking_calculator # custom hiking algorithm module
import re # imports regex module
app = Flask(__name__) # setup Flask application
app.secret_key = 'V|D4KN48$_706446s87fAdDdf#95783af2e8a' # setup Secret Key
int_regex = re.compile(r'^[0-9]*$') # regex pattern for integers onlys

#------------------------#
#----- Setup Routes -----#
#------------------------#
# Load Homepage (* Root Route *)
@app.route('/', methods=["GET","POST"])
def root():
    '''
    This route either gets loads the index page, or, (if the
    request method is a 'POST'), passes the data from the form
    through the hiking algorithm.
    '''
    # Check if request method is `POST` (via form submission):
    if request.method == 'POST':
        # Validate form:
        # Iterate through items in the form:
        for item in request.form:
            # Check if any form items are blank:
            if len(request.form[item]) < 1:
                # If so, send error:
                flash('All fields are required.')
                return redirect('/')
            # Check if any values are non-integers:
            elif not int_regex.match(request.form[item]): # if regex match fails:
                # Send error:
                flash('All fields must be numbers.')
                return redirect('/')

        # If so, run hiking algorithm:
        print 'Post method detected. Running Hiking Algorithm now...'
        hiking_data = {
            'distance': request.form['total_distance'],
            'gain': request.form['total_elev_gain'],
            'rest': request.form['hourly_break_duration'],
            'time': hiking_calculator.hiking_time(request.form['total_distance'], request.form['total_elev_gain'], request.form['hourly_break_duration'])
        }
        # Then, load root page again but with hiking_data from algorithm.
        return render_template('index.html', hiking_data = hiking_data)

    # If request method is get (default),load no hiking data:
    hiking_data = {}
    # Then, load root page without data:
    return render_template('index.html', hiking_data = hiking_data)

#-------------------------#
#----- Run Flask App -----#
#-------------------------#
'''
IMPORTANT: Be sure to REMOVE `debug` and `host` parameters below BEFORE DEPLOYING
otherwise, per QuickStart documentation, there are security issues.
'''
# Run Flask Application in Debug Mode:
app.run(debug=True, host='0.0.0.0')
