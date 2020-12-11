"""
Project model


Fiels:

    title:
        Project title

    description:
        Project description

    owners:
        Project owners (ManytoMany relation with user model)

    created_date:
        Creating date

    repo_url:
        Project's Repo Url (Github, bitbucket, sourceforge or others)
    
    starred_users:
        Users that starred this project

    comments:
        Project comments (Comment model)
"""

from django.db import models


class Project(models.Model):
    title = models.CharField(
        "Project Title",
        max_length=200,
        unique=True,
    )

    description = models.TextField(
        "Project Description",
        max_length=2000,
    )

    # TODO: Add owners field

    creating_date = models.DateField(
        "Creating Date",
        auto_now=True,
    )

    repo_url = models.URLField(
        "Repo URL",
    )

    # TODO: Add starred users field

    # TODO: Add comments relationship
