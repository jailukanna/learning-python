from __future__ import unicode_literals
from django.db import models

class ClientManager(models.Manager):
    """
    Extends `Manager` methods to add new clients.

    Parameters:
    - `models.Manager` - Gives us access to the `Manager` method to which we
    append additional custom methods.
    """

    def validate(self, **kwargs):
        """Validate and create new Client."""

        # Create errors list:
        errors = []

        # If any fields are empty, send back error:
        if len(kwargs["name"]) < 1 or len(kwargs["email"]) < 1 or len(kwargs["phone"]) < 1 or len(kwargs["notes"]) < 1:
            errors.append("All fields are required.")
            return errors


        try:
            # Check if client already exists:
            client = Client.objects.get(name=kwargs["name"])
            errors.append("Client already exists.")
            return errors
        except Client.DoesNotExist:
            # If client does not exist, make new client
            print "Client passed validation, creating new client..."
            new_client = Client(name=kwargs["name"], email=kwargs["email"], phone=kwargs["phone"], notes=kwargs["notes"])
            new_client.save()
            return new_client

class ProjectManager(models.Manager):
    """
    Extends `Manager` methods to add new projects.

    Parameters:
    - `models.Manager` - Gives us access to the `Manager` method to which we
    append additional custom methods.
    """

    def validate(self, **kwargs):
        """Validate and create new Project."""

        # Create errors list:
        errors = []

        # If any fields are empty, send back error:
        if len(kwargs["name"]) < 1 or len(kwargs["notes"]) < 1:
            errors.append("All fields are required.")
            return errors

        try:
            # Check if project already exists:
            project = Project.objects.get(name=kwargs["name"])
            errors.append("Project already exists.")
            return errors
        except Project.DoesNotExist:
            # If project does not exist, get current client and create project:
            print "Project passed validations...creating..."
            # Get current client:
            client = Client.objects.get(id=kwargs["client_id"])
            # Create new project:
            new_project = Project(name=kwargs["name"], notes=kwargs["notes"], client=client)
            new_project.save()
            # Send back new_project
            return new_project

class Client(models.Model):
    """Create new instances of a `Client`, which can possess many `Projects`."""

    name = models.CharField(max_length=50) # name
    email = models.CharField(max_length=50) # email
    phone = models.CharField(max_length=11) # phone
    notes = models.CharField(max_length=1000) # notes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()

class Project(models.Model):
    """Create new instances of a `Project`."""

    name = models.CharField(max_length=50) # name
    notes = models.CharField(max_length=1000) # notes
    client = models.ForeignKey(Client, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProjectManager()
