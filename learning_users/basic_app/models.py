from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    # Create one to one relationship (don't inherit from the User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # on_delete=models.CASCADE
    # This is the behaviour to adopt when the referenced object is deleted. It is not specific to django, this is an SQL standard.
    #  When the referenced object is deleted, also delete the objects that have references to it 

    # Additional attribues we want
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username