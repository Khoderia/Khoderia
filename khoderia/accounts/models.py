'''
User Model

Fields:

{Standard fields of user model}
'''

from django.db import models
from django.contrib.auth.models import AbstractUser
from projects.models.project_model import Project


class User(AbstractUser):
    # Methods
    def get_all_projects(self):
        """
        Returns all of the user's projects.
        """
        for project in Project.objects.all():
            if project 

