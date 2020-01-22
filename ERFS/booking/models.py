from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    asset_Title=models.CharField(max_length=50)
    asset_Type=models.CharField(max_length=20)
    asset_Price=models.IntegerField()
    asset_purpose=models.CharField(max_length=10)
    asset_Location=models.CharField(max_length=50)
    asset_Image=models.FileField(upload_to="assets/")
    def __str__(self):
        return self.asset_Title
class Booking(models.Model):
    asset=models.OneToOneField(Asset,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booking_Date=models.DateTimeField()
    booking_Status= models.BooleanField()
    def __str__(self):
        return self.booking_Date
class AddToFav(models.Model):
    user=models.ManyToManyField(User)
    asset=models.ManyToManyField(Asset)
    def __str__(self):
        return self.user