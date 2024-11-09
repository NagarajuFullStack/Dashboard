from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
# """A model to store user information."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
# OneToOneField is a type of
    id_number = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    portfolio_site = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    Email_address =models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)



    def __str__(self):
        return self.user.username
    



