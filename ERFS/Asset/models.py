from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Asset(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    asset_Title=models.CharField(max_length=50)
    asset_Type=models.CharField(max_length=20)
    asset_Price=models.IntegerField()
    asset_purpose=models.CharField(max_length=10)
    asset_Location=models.CharField(max_length=50)
    asset_Image=models.ImageField()
    def __str__(self):
        return self.asset_Title