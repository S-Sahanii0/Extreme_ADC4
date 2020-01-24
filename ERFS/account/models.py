from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile/images/")
    bio=models.TextField(max_length=100)
    




