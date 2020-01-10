from django.db import models
# Create your models here.

class Seller(models.Model):
    seller_Name=models.CharField(max_length=30)
    seller_Contact=models.IntegerField()
    seller_Address=models.CharField(max_length=40)

    def __str__(self):
        return self.seller_Name

class Buyer(models.Model):
    buyer_Name=models.CharField(max_length=30)
    buyer_Contact=models.IntegerField()
    buyer_Address=models.CharField(max_length=40)

    def __str__(self):
        return self.buyer_Name
