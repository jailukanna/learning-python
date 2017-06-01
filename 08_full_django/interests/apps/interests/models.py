# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    """
    Extends `Manager` methods to add new users and interests.

    Parameters:
    - `models.Manager` - Gives us access to the `Manager` method to which we
    append additional custom methods.

    Functions:
    -
    """

    def validate(self, **kwargs):
        """
        Checks for existing user, and if so, for existing interest.

        Validations:
        - Both fields required, at least 2 char.
        - If user exists, only add interest if unique.
        - If user does not exist, create interest and user, and associate interest to user.
        """

        # Create errors list:
        errors = []

        # Check if any fields are empty:
        if len(kwargs["name"]) < 2 or len(kwargs["interest"]) < 2:
            errors.append("Both fields are required and must be at least 2 characters.")
            return errors
            
        # Check if existing user:
        print "Checking for existing user..."
        for user in User.objects.all():

            # Check if existing user's name matches form submission name:
            if user.name == kwargs["name"]:
                print "Found existing user..."
                # Retrieve existing user:
                existing_user = User.objects.get(name=kwargs["name"])
                # Check if interest already exists for retrieved user:
                for interest in existing_user.interests.all():
                    if interest.description == kwargs["interest"]:
                        print "Error: Existing interest found"
                        print "Cannot add interest, already exists."
                        errors.append("Interest already exists for this user.")
                        return errors
                # If interest does not already exist:
                print "No existing interest found..."
                print "Creating new interest..."
                new_interest = Interest(description=kwargs["interest"])
                new_interest.save()
                # Add new interest to retrieved user's interests:
                existing_user.interests.add(new_interest)
                # Send back:
                return existing_user
        # If user is not found create user and interest, and add interest to user's interests:
        print "Existing user was not found..."
        print "Creating interest and user now..."
        # Create interest:
        new_interest = Interest(description=kwargs["interest"])
        new_interest.save()
        # Create user:
        new_user = User(name=kwargs["name"])
        new_user.save()
        # Add interest to user's interests:
        new_user.interests.add(new_interest)
        return new_user

class Interest(models.Model):
    """Create new instances of an `Interest` which may belong to a user."""

    description = models.CharField(max_length=300) # interest description
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    """Create new instances of a `User` with interests."""

    name = models.CharField(max_length=50) # user's name
    interests = models.ManyToManyField(Interest, related_name="user") # many-to-many interest (user can have many interests) - related name `users` will help with reverse lookup when looking for `Interest.users`
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() # Attaches helpful `UserManager` methods to our `User.objects` object (so we can access these methods in our controller).
