
1. Activate Required Virtual Environment and Generate `requirements.txt`:
    - Navigate into root of project directory.
    - Start your VENV
    - `pip freeze > requirements.txt` to generate `requirements.txt`
    - Remove `pygraphviz`, `pydot` and anything with `MySQL` in it.

2. Create a Git Repository and Push Project:
    - Create a `.gitignore` file.
        - Add the lines:
            `*.pyc
            venv/
            .DS_Store`
    - Init and Commit a Repo to your online Repo. Push to online repo.
    - Make sure to `git remote add origin`

3. Start and Launch an EC2 Instance:
    - Select Ubuntu 16.04, t2 Micro
    - Security Settings: `Anywhere` for HTTP and HTTPS
    - Security Settings: SSH could be setup for your IP only.
    - Select Django Key File.
    - Launch Instance.

4. Connect to Instance via SSH:
    - Navigate into AWS-KEYS directory in terminal. (where your key file is stored)
    - Click blue "Connect" button. Paste this SSH stuff into terminal.

5. Install `python`, `python` `dev`, `pip`, `nginx`, and `git` on your AWS box:
    `sudo apt-get update`
    - update apt-get

    `sudo apt-get install python-pip python-dev nginx git`
    - install python, pip, nginx, git

    `sudo apt-get update`
    - update apt-get again after we've installed everything

    `sudo pip install virtualenv`
    - install virtualenv

6. Clone your Git Repo onto your Ubuntu Box:
    - git clone `https://github.com/username/project.git`
    - At the moment, your current folder directory should look something like this.

        + ubuntu
          + repoName
            + apps
            + projectName
            + ...# other files/folders

    - Navigate into this project and run `ls` in your terminal.
    - If you don’t see `manage.py` as one of the files, STOP. Review the setting up GitHub/Git pieces from earlier.

7. If everything looks good, make the virtual environment, and activate it.

    `ubuntu@54.162.31.253:~/myRepoName$ virtualenv venv`
    `ubuntu@54.162.31.253:~/myRepoName$ source venv/bin/activate`
    `(venv)ubuntu@54.162.31.253:~/myRepoName$ pip install -r requirements.txt`
    `(venv) ubuntu@54.162.31.253:~/myRepoName$ pip install django bcrypt django-extensions`
    `(venv) ubuntu@54.162.31.253:~/myRepoName$ pip install gunicorn`

8. Edit Settings.py

    `(venv) ubuntu@54.162.31.253:~/myRepoName$ cd {{projectName}}`
    `(venv) ubuntu@54.162.31.253:~/myRepoName/projectName$ sudo vim settings.py`

    - Once inside:

        + Inside settings.py
        + Modify these lines:
            `DEBUG = False`
            `ALLOWED_HOSTS = ['{{yourEC2.public.ip}}']`
        + Add the line below to the bottom of the file:
            `STATIC_ROOT = os.path.join(BASE_DIR, "static/")`
        + Save changes and quit.

        + To get back to folder with manage.py
            `cd ..`

    Run "collect static":
    `(venv) ubuntu@54.162.31.253:~myRepoName$ python manage.py collectstatic #say yes`

9. Setup Gunicorn:

    - Direct gunicorn to wsgi file:
    `(venv) ubuntu@54.162.31.253:~myRepoName$ gunicorn --bind 0.0.0.0:8000 {{projectName}}.wsgi:application`

    - Exit process:
    `ctrl-c`

    - Deactivate your virtual env:
    `deactivate`

    - Setup Gunicorn to run as a service (so that it will always start with the server):
    (otherwise you'd have to manually start it every time):
        + Create a systemd service file:
            `ubuntu@54.162.31.253:~myRepoName$ sudo vim /etc/systemd/system/gunicorn.service`
        + In the VIM editor, copy and paste the following code:
            `[Unit]
            Description=gunicorn daemon
            After=network.target
            [Service]
            User=ubuntu
            Group=www-data
            WorkingDirectory=/home/ubuntu/{{repoName}}
            ExecStart=/home/ubuntu/{{repoName}}/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/{{repoName}}/{{projectName}}.sock {{projectName}}.wsgi:application
            [Install]
            WantedBy=multi-user.target`
        + Save and close the file.
        + Enable the service so it starts on boot:
            `ubuntu@54.162.31.253:~$ sudo systemctl daemon-reload`
            `ubuntu@54.162.31.253:~$ sudo systemctl start gunicorn`
            `ubuntu@54.162.31.253:~$ sudo systemctl enable gunicorn`
        + Note: if any additional changes are made to the gunicorn.service the previous three commands will need to be run in order to sync things up and restart our service.

10. Setup Nginx:
    + Open Nginx config file:
    `ubuntu@54.162.31.253:~$ sudo vim /etc/nginx/sites-available/{{projectName}}`

    + Add the following:
    `server {
        listen 80;
        server_name {{yourEC2.public.ip}};
        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
          root /home/ubuntu/{{myRepoName}};
        }
        location / {
            include proxy_params;
            proxy_pass http://unix:/home/ubuntu/{{myRepoName}}/{{projectName}}.sock;
        }
    }`

    + Save and exit.

    + Now in the terminal, run the following (taking note of the space after {{projectName}}):

        `ubuntu@54.162.31.253:~$ sudo ln -s /etc/nginx/sites-available/{{projectName}} /etc/nginx/sites-enabled`
        `ubuntu@54.162.31.253:~$ sudo nginx -t`

11. Remove Default Nginx and Restart Server:
    + Remove nginx default site display from directory sites-enabled:
        `ubuntu@54.162.31.253:~$ sudo rm /etc/nginx/sites-enabled/default`
    + Restart server:
        `54.162.31.253:~$ sudo service nginx restart`
    + If your server restarted correctly, you will see the new command line, and your app is deployed!
    + Go to the public domain and your app should be there.
    + If you see anything other than your app, review your server file for errors.

12. Common Errors:
    + 502, bad gateway: there is a problem in your code. Hint: any error starting with 5 indicates a server error
    + Your Gunicorn process won’t start: Check your .service file; typos and wrong file paths are common mistakes
    + Your NGINX restart fails: Check your NGINX file in the sites-available directory. Common problems include typos and forgetting to insert your project name where indicated.

13. Add in MySQL:
    + First, must install everything we need to run MySQL:
    `ubuntu@54.162.31.253:~$ sudo apt-get install libmysqlclient-dev`

    + Install `MySQL-server`:
        `ubuntu@54.162.31.253:~$ sudo apt-get install mysql-server`
        + enter `root` as password

    + Switch to root user:
        `ubuntu@54.162.31.253:~$ sudo su`

    + Open MySQL command line:
        `ubuntu@54.162.31.253:~$ mysql -u root -p`

    + Create a database for this project:
        `CREATE DATABASE {{projectName}};` # note the semi-colon

    + Exit the MySQL prompt:
        `exit;`

    + Deactivate the root user:
        `exit` # no semi-colon
        *CRITICAL STEP*

    + Enter project folder so we may access `settings.py`:
        `ubuntu@54.162.31.253:~$ cd {{projectName}}`

    + Activate your virtualenv:
        `source venv/bin/activate`

    + Install a pip module so we may connect our python code to our mysql code:
        `(venv) ubuntu@54.162.31.253:~$ pip install mysql-python`

    + Open up `settings.py` and configure your database:
        `sudo vim settings.py`

        - Change the databases section to look like this:
        `DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': '{{projectName}}',
                'USER': 'root',
                'PASSWORD': 'root',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }`
        - Save and exit vim.

    + Make migrations:
        `(venv) ubuntu@54.162.31.253:~myRepoName$ python manage.py makemigrations`
        `(venv) ubuntu@54.162.31.253:~myRepoName$ python manage.py migrate`

    + Restart Nginx:
        `sudo service nginx restart`

    + Now visit your site! You should be finished at this point, with a fully functioning site.
    + Your old data will *not* show up, but you should be able to perform all operations as you did previously.
