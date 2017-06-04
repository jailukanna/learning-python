from django.shortcuts import render, redirect
from django.contrib import messages # provides access to django's `messages` module.
from models import Client, Project # provides access to Client, Project models.

def index(request):
    """Load homepage and main dashboard."""

    all_clients = {
        "all_clients": Client.objects.all()
    }
    return render(request, "client_resources/index.html", all_clients)

def add_client(request):
    """If GET request, load add client form; if POST, create new client."""


    if request.method == "GET":
        return render(request, "client_resources/add_client.html")
    else:
        client_data = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "phone": request.POST["phone"],
            "notes": request.POST["notes"],
        }
        new_client = Client.objects.validate(**client_data)

        if type(new_client) is list:
            # Generate errors if list is returned:
            for error in new_client:
                messages.error(request, error)
            return redirect('/client/add')
        else:
            # New Client has been generated successfully, load client show page:
            return redirect('/client/' + str(new_client.id))

def show_client(request, id):
    """Get client by ID and load client information (show) page."""

    client = {
        "client": Client.objects.get(id=id),
        "projects": Client.objects.get(id=id).projects.all()
    }
    return render(request, "client_resources/show_client.html", client)

def add_project(request, id):
    """Retrieve client by ID--if GET, load add project form; if POST, create new project and assign to client."""

    # Get current client:
    client = {
        "client": Client.objects.get(id=id),
    }

    # If post method, create new project for client:
    if request.method == "POST":
        print "Post method detected..."
        # Organize data prior to project creation:
        project_data = {
            "name": request.POST["name"],
            "notes": request.POST["notes"],
            "client_id": id,
        }
        # Create new project / validate:
        new_project = Project.objects.validate(**project_data)

        if type(new_project) is list:
            # Generate errors if list is returned:
            for error in new_project:
                messages.error(request, error)
            return redirect('/' + id + '/addproject')
        else:
            # New Project has been generated successfully, load project show page:
            project = {
                "new_project": new_project,
            }
            return redirect('/show/projects/' + str(project["new_project"].id))
    else:
        print "Get request detected...loading add project form...."
        # Request was a GET, load add project page:
        return render(request, "client_resources/add_project.html", client)


def show_project(request, id):
    """Get project by ID and load project information (show) page."""

    project = {
        "project": Project.objects.get(id=id),
    }

    return render(request, "client_resources/show_project.html", project)
