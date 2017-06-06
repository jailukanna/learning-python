from django.shortcuts import render, redirect
from django.contrib import messages # provides access to django's `messages` module.
from models import Client, Project # provides access to Client, Project models.

def index(request):
    """Retrieve all clients and load dashboard homepage."""

    # Get all clients;
    all_clients = {
        "all_clients": Client.objects.all()
    }
    # Load dashboard:
    return render(request, "client_resources/index.html", all_clients)

def add_client(request):
    """If GET request, load add client form; if POST, create new client."""

    # If GET, load add client form:
    if request.method == "GET":
        return render(request, "client_resources/add_client.html")
    else: # If POST, validate and create new client:
        # Prepare data for client validation/creation:
        client_data = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "phone": request.POST["phone"],
            "notes": request.POST["notes"],
        }

        # Validate and create client.
        # If validation fails, return a list of errors.
        # If validation succeeds, return new client Object:
        new_client = Client.objects.validate(**client_data)

        # Check if new_client data is list of errors:
        if type(new_client) is list:
            # Generate errors:
            for error in new_client:
                messages.error(request, error)
            # Reload client add page with errors:
            return redirect('/client/add')
        else: # Otherwise if new_client is returned, load client show page:
            return redirect('/client/' + str(new_client.id))

def show_client(request, id):
    """Get client and client's projects, load client show page."""

    # Get client and all projects belonging to client:
    client = {
        "client": Client.objects.get(id=id),
        "projects": Client.objects.get(id=id).projects.all()
    }
    # Load client show page:
    return render(request, "client_resources/show_client.html", client)

def add_project(request, id):
    """If GET, load add project form; if POST, create new project and assign to client."""

    # If post method, create new project for client:
    if request.method == "POST":
        print "Organizing project data..."
        # Organize data prior to project validation/creation:
        project_data = {
            "name": request.POST["name"],
            "notes": request.POST["notes"],
            "client_id": id,
        }
        # Create new project/validate.
        # If validation fails, a list of errors is returned.
        # If validation succeeds, the new project Object is returned:
        print "Validating and creating project data..."
        new_project = Project.objects.validate(**project_data)

        # Check if errors list is returned:
        if type(new_project) is list:
            print "Errors validating."
            # Generate errors if list is returned:
            for error in new_project:
                print error
                # Add error to django messaging:
                messages.error(request, error)
            # Reload add project form with errors:
            return redirect('/' + id + '/addproject')
        else: # If no errors, redirect to project show route:
            print "Project has been created."
            # Redirect to project show route.
            # Note: The new project `id` is also sent, so that the project may be retreived for the show page route:
            return redirect('/show/projects/' + str(new_project.id))
    else: # If not a post method, load add project form with retrieved current client:
        print "Loading add project form...."
        # Get current client:
        client = {
            "client": Client.objects.get(id=id), # Gets client by `id`
        }
        # Load add project form with current client:
        return render(request, "client_resources/add_project.html", client)


def show_project(request, id):
    """Get project by ID and load project information (show) page."""

    # Get project by ID:
    project = {
        "project": Project.objects.get(id=id),
    }

    # Load show project page with retrieved project:
    return render(request, "client_resources/show_project.html", project)
