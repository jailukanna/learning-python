
# AWS Django Deployment, Ubuntu 16.04:
### Updated: November 2017

The steps below outline how to take a Django project and deploy it on an AWS box
running Ubuntu 16.04. Note: A free AWS account is required prior to starting this tutorial.

*Note: This file may be updated in the future, as new versions of Ubuntu are released,
or if there are any changes to required modules*

1. Activate Required Virtual Environment and Generate `requirements.txt`:
    - Navigate into root of project directory.
    - Start your VENV.
    - `pip freeze > requirements.txt` to generate `requirements.txt`.
    - Remove `pygraphviz`, `pydot` and anything with `MySQL` in it.

2. Create a Git Repository and Push Project:
    - Create new git repository on github.com.
    - Create new git repository in project folder.
    - Create a `.gitignore` file.
        - Add the lines:
            `*.pyc
            venv/
            .DS_Store`
    - Add your remote repository: `git remote add origin`
    - `git add .` to add all files.
    - `git commit -m "my first commit"` to commit.
    - `git push -u origin master` to push.

3. Start and Launch an EC2 Instance:
    - Select Ubuntu 16.04, t2 Micro
    - Security Settings: `Anywhere` for HTTP and HTTPS
    - Security Settings: SSH could be setup for your IP only.
    - Select Django Key File.
    - Launch Instance.

4. Connect to Instance via SSH:
    - Navigate into AWS-KEYS directory in terminal. (where your key file is stored)
    - Click blue "Connect" button. Paste this SSH stuff into terminal.
    - *Note: If receiving `NOT ALLOWED` message, open up the file in the log bug and clear out any RSA entries for the AWS SSH address. This will force a new RSA signature*

5. Install `python`, `python` `dev`, `pip`, `nginx`, and `git` on your AWS box:
    - Update apt-get: `sudo apt-get update`

    - Install python, pip, nginx, git: `sudo apt-get install python-pip python-dev nginx git`

    - Update apt-get again after we've installed everything: `sudo apt-get update`

    Install virtualenv:
    - `sudo -H pip install --upgrade pip`
    - `sudo -H pip install virtualenv`
    
    If wishing to **use Virtualenvwrapper**:
    - `sudo pip install virtualenvwrapper`
    - `export WORKON_HOME=~/Envs` # sets up virtualenvwrapper
    - `source /usr/local/bin/virtualenvwrapper.sh` # sets up virtualenvwrapper
        Update your ubuntu user profile so you don't have to re-run the virtualenvwrapper setup every time:
        - `cd ~`
        - `ls -a` (shows hidden files)
        - `sudo vim .profile`
        - Add these two lines to the very bottom of the file:
            - `export WORKON_HOME=~/Envs` # sets up virtualenvwrapper
            - `source /usr/local/bin/virtualenvwrapper.sh` # sets up virtualenvwrapper
        - Hit `Esc` key and type `:wq` to save and exit file.
        
    If **NOT using Virtualenvwrapper**:
    - `virtualenv venv`    

6. Clone your Git Repo onto your Ubuntu Box:
    - git clone https://github.com/username/project.git
    - At the moment, your current folder directory should look something like this.

        + ubuntu
          + repoName
            + apps
            + projectName
            + ...# other files/folders

    - Navigate into this project and run `ls` in your terminal.
    - If you don’t see `manage.py` as one of the files, STOP. Review the setting up GitHub/Git pieces from earlier.

7. If everything looks good, make the virtual environment, activate it and pip install.

    **If using Virtualenvwrapper:**
    - If virtualenvwrapper with *Python 3*:
      + `which python3`
      + (Should give output: /usr/bin/python3)
      + `mkvirtualenv --python=/usr/bin/python3 {{virtualenvNAME}}` 
      + (Python3 will now be set to default for `python` command and your virtualenv will setup utilizing py3 modules.)
        
    - If virtualenvwrapper with *Python 2*:
      + `mkvirtualenv {{my_virtual_environment}}` # creates virtualenv
            
    - Once virtualenv is setup for either py2 or py3:
      + `workon {{my_virtual_environment}}` # starts virtualenv    
        
    **If NOT using Virtualenvwrapper:**
      + `source venv/bin/activate`

    Install all pip packages, django, bcrypt, and gunicorn:
    - `pip install -r requirements.txt` # installs files from requirements.txt -- *do not run these commands as sudo*
    - `pip install django bcrypt django-extensions`
    - `pip install gunicorn` # install green unicorn

8. Edit Settings.py
    - `cd {{projectName}}`
    - `sudo vim settings.py`
    
    - Once inside:
      + Inside settings.py
      + Modify these lines:
          - `DEBUG = False`
          - `ALLOWED_HOSTS = ['{{yourEC2.PUBLIC.ip}}', '{{sub.domain}}', '{{www.sub.domain}}']`
      + Add the line below to the bottom of the file:
          - `STATIC_ROOT = os.path.join(BASE_DIR, "static/")`
      + Save changes and quit.
          - `Esc`, `:wq`
      + To get back to folder with manage.py
          - `cd ..`
    
    - Run "collect static":
      + `python manage.py collectstatic` # say yes -- collects all static files
    
    *Personal Note: Adding any or updating fav icons may require you to run this command again, else django won't update static files.                  This may be true for adding images or image sets as well, or any static file, although I've only experienced this need thus far when changing fav icons.*

9. Setup Gunicorn:

    - Direct gunicorn to wsgi file: `gunicorn --bind 0.0.0.0:8000 {{projectName}}.wsgi:application`
    - Exit process: `ctrl-c`
    - Deactivate your virtual env: `deactivate`
    - Setup Gunicorn to run as a service (so that it will always start with the server):
        (otherwise you'd have to manually start it every time):
      + Create a systemd service file:
          - `sudo vim /etc/systemd/system/gunicorn.service`
      + In the VIM editor, copy and paste the following code, *update* all variables in `{{curly brackets}}`:
      ````
      [Unit]
      Description=gunicorn daemon
      After=network.target
      [Service]
      User=ubuntu
      Group=www-data
      WorkingDirectory=/home/ubuntu/{{repoName}}
      ExecStart=/home/ubuntu/Envs/{{virtualenvNAME}}/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/{{repoName}}/{{projectName}}.sock {{projectName}}.wsgi:application
      [Install]
      WantedBy=multi-user.target
      ````       

    *Notes About Config File:*
    - *Make sure the above is not indented.*
    - *Make sure that gunicorn `ExecStart` path is correctly pointing to your virtualenv directory.
    - In our case, `home/ubuntu/Envs/{{virtualenv_name}}` -- this is due to use of `virtualenvwrapper`*
    - **IMPORTANT IF NOT USING VIRTUALENVWRAPPER**: Because virtualenvwrapper creates a little different folder structure, if choosing NOT to utilize it, be sure to updated the `ExecStart` line in the config file above to the following instead:
    ```
    ExecStart=/home/ubuntu/{{repoName}}/{{virtualenvNAME}}/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/{{repoName}}/{{projectName}}.sock {{projectName}}.wsgi:application
    ```
    *Note: The virtual environment path is different when not using virtualenvwrapper*
    - Save and close the file.
        
    Enable the service so it starts on boot:
    - `sudo systemctl daemon-reload`
    - `sudo systemctl start gunicorn`
    - `sudo systemctl enable gunicorn`
        
    *Note: If any additional changes are made to the gunicorn.service the previous three commands will need to be run in order to sync things up and restart our service.*

10. Setup Nginx:
    + Open Nginx config file:
    - `sudo vim /etc/nginx/sites-available/{{projectName}}`

    + Add the following (be sure to update variables in the `{{curly_brackets}}`'s'):
    ```
    server {
        listen 80;
        server_name {{yourEC2.PUBLIC.ip}} {{sub.domain}} {{www.sub.domain}};
        error_log /var/log/nginx/error.log warn;  # you can change `warn` to `debug` if you need detailed info
        access_log /var/log/nginx/access.log;
        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
          root /home/ubuntu/{{myRepoName}};
        }
        location / {
            include proxy_params;
            proxy_pass http://unix:/home/ubuntu/{{myRepoName}}/{{projectName}}.sock;
        }
    }
    ```

    + Save and exit.

    + Now in the terminal, run the following (taking note of the space after `{{projectName}}`):

        - `sudo ln -s /etc/nginx/sites-available/{{projectName}} /etc/nginx/sites-enabled`
        - `sudo nginx -t`

11. Remove Default Nginx and Restart Server:
    + Remove nginx default site display from directory sites-enabled:
        - `sudo rm /etc/nginx/sites-enabled/default`
    + Restart server:
        - `sudo service nginx restart`
    + If your server restarted correctly, you will see a new command line (no error, just a blinking cursor), and your app is deployed!
    + Go to the public domain and your app should be there.
    + If you see anything other than your app, review your server file for errors.

12. Common Errors:
    + `502, bad gateway`: there is a problem in your code. Hint: any error starting with 5 indicates a server error
    + See `/var/log/nginx` folder for `error.log` and `access.log` for log files for errors and http requests. 
    + Update your nginx config and change your error.log from `warn` to `debug` for more detailed info.
    + Make sure you've restarted nginx, or if you've changed gunicorn settings, that you restart gunicorn.
    + Try restarting the system via `sudo reboot`. This will close your AWS connection while the virtual instance restarts.
    + If you updated an A record, be patient, it may take an hour or more, or even longer if you made multiple A record updates. Take a breakd and step back and return.
    + Your Gunicorn process won’t start: Check your .service file; typos and wrong file paths are common mistakes
    + Your NGINX restart fails: Check your NGINX file in the sites-available directory. Common problems include typos and forgetting to insert your project name where indicated.

13. Updating your Codebase:
    + You can update your codebase by using `sudo git pull origin master` from within your `/var/www/{{project_directory}}` folder. This will pull your changes from GitHub/your repo but will not wipe out your settings.py changes, server configs, etc.
    + **DO NOT** `git add`, or `git commit` from your repo to the main branch. This will overwrite your development settings.py with your production settings.py.
    + **DO NOT** `git stash` changes either, as this will pull your settings.py and wipe out your production settings.
    + *You may want to create two seperate branches, one for development and one for production, and push your development branch to your production branch, and when doing so, discard any changes to settings.py etc*

14. Add in MySQL:

    **WARNING: I have not successfully been able to utilize these directions for MySQL. May have to try again or research and update the write-up below. Proceed at your own risk.**

     + First, must install everything we need to run MySQL:
     - `sudo apt-get install libmysqlclient-dev`

     + Install `MySQL-server`:
         - `sudo apt-get install mysql-server`
         + enter `root` as password

     + Switch to root user:
         - `sudo su`

     + Open MySQL command line:
         - `mysql -u root -p`

     + Create a database for this project:
         - `CREATE DATABASE {{projectName}};` # note the semi-colon
    
     + Exit the MySQL prompt:
         - `exit;`

     + Deactivate the root user:
         - `exit` # no semi-colon
         *CRITICAL STEP*

     + Enter project folder so we may access `settings.py`:
         - `cd {{projectName}}`

     + Activate your virtualenv:
         - `source venv/bin/activate`

     + Install a pip module so we may connect our python code to our mysql code:
         - `pip install mysql-python`

        + Open up `settings.py` and configure your database:
            - `sudo vim settings.py`

         - Change the databases section to look like this:
         ```
         DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': '{{projectName}}',
                'USER': 'root',
                'PASSWORD': 'root',
                'HOST': 'localhost',
                'PORT': '3306',
            }
         }
         ```
         - Save and exit vim.

     + Make migrations:
         - `cd ..` # go back to your root project directory
         - `python manage.py makemigrations` # setup migrations
         - `python manage.py migrate` # make migrations

     + Restart Nginx:
          `sudo service nginx restart`

     + Now visit your site! You should be finished at this point, with a fully functioning site.
     + Your old data will *not* show up, but you should be able to perform all operations as you did previously.
