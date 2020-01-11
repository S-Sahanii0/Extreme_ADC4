from django.db import models
from endUser.models import Seller, Buyer

class Asset(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    asset_Title=models.CharField(max_length=50)
    asset_Type=models.CharField(max_length=20)
    asset_Price=models.IntegerField()
    asset_purpose=models.CharField(max_length=10)
    asset_Location=models.CharField(max_length=50)
    asset_Image=models.ImageField()
    def __str__(self):
        return self.asset_Title
class Booking(models.Model):
    asset=models.OneToOneField(Asset,on_delete=models.CASCADE)
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    booking_Date=models.DateTimeField()
    booking_Status= models.BooleanField()
    def __str__(self):
        return self.booking_Date
class AddToFav(models.Model):
    buyer=models.ManyToManyField(Buyer)
    asset=models.ManyToManyField(Asset)
    def __str__(self):
        return self.buyer
