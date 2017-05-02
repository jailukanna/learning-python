# How To Setup Django Projects:
// Coding Dojo, September 2016, Tim Knab

## Part 1: Setup Django and Configure Application and Run Server:

    1. Start your Django virtual env go to the folder where you want your project to be created:

    2. Once in your desired root folder for your project, in terminal:

        `django-admin startproject <my_project>`

        **Notes**
        + This creates a new project with the folder name `<my_project>` -- change this to whatever you'd like your project to be
        + When this folder is created, some default Django files will automatically be added and a subfolder with the same name will be created
        + Don't be afraid as you see all these weird new files now (this is Django having built itself)


    3. Navigate inside of your `<my_project>` folder and create a folder called `apps` and add an empty `__init__.py` so the folder is recognized:


        + Navigate into your project folder (note, `<my_project>` refers to the name you you created)
        `cd <my_project>`

        + Make a folder called `/apps` inside of `/<my_project>`
        `mkdir apps`

        + Go into apps
        `cd apps`

        + Create a blank __init__.py file in /apps:
        `touch __init__.py`


    4. Unpack your application files into `/apps/<my_app>` folder:

        + Make sure you're inside of your /apps folder and type:
        `python ../manage.py startapp <first_app>`

        + `<first_app>` folder is created inside of `/apps` and Django Python files are added
        + You can name `<first_app>` whatever you want -- maybe a short hand of `<my_project>`
        + currently no routes are setup, etc, but your server should run
        + You can run your server and check if you want

    5. Configure `<my_project>/<my_app>/settings.py` file to hook up your application:

        + Navigate to `<my_project>/<my_app>/settings.py`
        + In `settings.py`, we need to add our app to the list of applications so its hooked in.
        + Open `settings.py` by typing into terminal:
            `vi settings.py`

        + Edit the file as follows:
            - Add `apps.<first_app>` to our `INSTALLED_APPS` list:
            - `<first_app>` should match the name of `my_app` in: `<my_project>/apps/<my_app>`

            - Inside `<my_project>/settings.py`:
                `INSTALLED_APPS = [
                   'apps.<first_app>', ### added this line! * MAKE SURE TO INCLUDE COMMA AFTER OR APP WON'T WORK *
                   'django.contrib.admin',
                   'django.contrib.auth',
                   'django.contrib.contenttypes',
                   'django.contrib.sessions',
                   'django.contrib.messages',
                   'django.contrib.staticfiles',
               ]`

            - Once edits are complete, hit `esc` to exit insert mode and then type `:wq` to save and exit (or type `shift+z+z` from command mode)

    6. Goto `<my_project>` and run server:
        `cd ..`
        `python manage.py runserver` from the terminal.

    7. Load up `http://localhost:8000`.
        + You should see a welcome message.
        + Good to test server just in case -- can run migrations now too if using session or any needed components








## Part 2: Setup Templates and Static Folders for Templating:


    1. Create your `/templates` and `/static` folders inside `<my_app>`:
        + Navigate to `<my_project>/apps/<my_app>`
        + Create `<my_project>/apps/<my_app>/templates` directory
            `mkdir templates`
        + Create `<my_project>/apps/<my_app>/static` directory
            `mkdir static`

    2. Setup `<my_app>` folder inside `<my_project>/apps/<my_app>/templates`:
        + We must use the same name of our project and create a directory
        inside both our `/templates` and our `/static` folders.
        + This is because Django is modularized and setup so many apps
        can run on the same project.
        + In our case, we'll only have one folder in there for now, but
        we need to modularize it anyhow:
        + Create directory `<my_project>/apps/<my_app>/templates/<my_app>/`:
            `cd templates`
            `mkdir <my_app>`
        + **Warning**: `<my_app>` folder name must match `<my_project>/apps/<my_app>` folder name
        + ie, both `<my_app>` must be the same name.

    3. Add a basic HTML template:
        + Create an empty `index.html` file inside of `<my_project>/apps/<my_app>/templates/<my_app>`:
            `cd <my_app>`
            `touch index.html`

    4. Navigate back to `apps/<my_app>` and do the same for the `<my_project>/apps/<my_app>/static` folder:
        `cd ..`
        `cd ..`
        `cd static`
        `mkdir <my_app>`

    5. Create static file subfolders inside of `<my_project>/apps/<my_app>/static/<my_app>`:
        + This is important for modularizing your static files:
            `cd <my_app>`
            `mkdir images`
            `mkdir js`
            `mkdir css`
        + Navigate back to `<my_project>/apps/<my_app>` folder:
            `cd ..`
            `cd ..`
        + If these sub-folders are never used to store static content, you can delete them at a later time.









## Part 3: 1 of 2: Setup Controller (aka, Django calls it 'View') which consists of `urls.py`:
    + This is where we will catch our url routes (think of this is as the `routes.js` equivalent in MEAN)
    1. Create a blank `urls.py` file in `<my_project>/apps/<my_app>`:
    2. Make sure in `<my_project>/apps/<my_app>` and confirm `urls.py` does not exist:
        `ls`
    3. Create `urls.py` if it does not exist:
        `touch urls.py`
    4. We will build data into this file later
    5. Navigate back to `/<my_project>` and launch editor:
        `cd ..`
        `cd ..`
        `atom .`
    6. In your editor, open `<my_project>/<my_project>/urls.py`:
        **This is not the file you just created - it's a different `urls.py`**
        **Be sure you are working in the `urls.py` file which already has pre-loaded Django content.**
        + We need to point it to get the routes from `apps/<my_app>`:
        + Update the file, so it looks like this:
            `from django.conf.urls import url, include

            urlpatterns = [
              url(r'^', include("apps.<my_app>.urls"))
            ]`

            **Notes:**
            - Notice we added `include`.
            - We use `include` to pull in our `apps.<my_app>.urls` file - make sure you enter this in a string format
            - We removed any references to the `django admin`
            - Notice the regex pattern `r'^'` contains NO `$` symbol

        + After editing *save* and *Edit > Select All* (CMD + A)
        + Copy the entire contents of the file for the next step!

    7. Configure `<my_project>/apps/<my_app>/urls.py` file:
        + Open `<my_project>/apps/<my_app>/urls.py`:
            - Paste in the contents of your `<my_project>/<my_project>/urls.py`
            - Edit the file as follows:
                + Remove `include` from the `import` statement
                + Add the line:
		            - `from . import views`
                    - This will import our `views.py` (that we are going to build last)
                    - `views.py` is also where we put our Routes
                + Change `urlspattern` as follows:
                    `urlpatterns = [
                        url(r'^$', views.index),
                    ]`

                    **Notes:**
                    - Make sure to include the $ in your regex pattern
                    - Notice `views.index` points to the index method in your `views.py` file
                    - *we'll have to create that index method in `views.py` or nothing will work*
                    - You don't have to use `.index` as the method name, you can use another, but make sure
                      whatever name you choose is properly defined in your `apps/<my_app>/views.py` file









## Part 4: 2 of 2: Setup Controller (aka, Django calls it 'View') which consists of `views.py`:
    + This is where our route methods will be defined, and is considered a part of the `Controller` / `View` (`view` in the MTV sense, not the MVC sense.)
    1. Open `<my_project>/apps/<my_app>/views.py` file
    2. Create your views:
    3. The first view you'll want to create will be to handle your `index` method:
    4. The following `index` method will render the `templates/<my_app>/index.html` page as follows:

        `def index(request):
        	return render(request, '<my_app>/index.html')`

        **Notes**:
        + Be sure to open your `index.html` file and add some content.
        + If `def index(request)` is not defined, the `views.index` in `/apps/<my_app>/urls.py` won't point to anything.
        + Make sure your method name matches the name you used in your `urls.py` file (ie, we used `view.index`, `index` being the `index()` method defined in our `views.py`)







## Part 5: Launch your Django Application:
    1. Make sure your `index(request`) method has been properly defined.
    2. Restart your server, your `templates/apps/<my_app>/index.html` page should load (or whatever page you defined in your method)
