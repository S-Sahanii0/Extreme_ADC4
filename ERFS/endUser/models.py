from django.db import models
# Create your models here.

class EndUser(models.Model):
    username=models.CharField(max_length=10)
    Name=models.CharField(max_length=30)
    Contact=models.IntegerField()
    Address=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

    def __str__(self):
        return self.username
