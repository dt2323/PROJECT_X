from django.db import models
from django.contrib import auth

# Create your models here.

#This a class for users, using Django's built in models.
#We can use this for user forms so Django takes care of the backend/
class User(auth.models.User, auth.models.PermissionsMixin):
    #This is to create a string representation of the user.
    def __str__(self):
        return "@{}".format(self.username)
