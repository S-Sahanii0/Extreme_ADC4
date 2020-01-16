from django.db import models
# Create your models here.

class Seller(models.Model):
    userName=models.CharField(max_length=10)
    seller_Name=models.CharField(max_length=30)
    seller_Contact=models.IntegerField()
    seller_Address=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

    

    def __str__(self):
        return self.userName

class Buyer(models.Model):
    userName=models.CharField(max_length=10)
    buyer_Name=models.CharField(max_length=30)
    buyer_Contact=models.IntegerField()
    buyer_Address=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

    def __str__(self):
        return self.userName
