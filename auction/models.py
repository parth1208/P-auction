from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Profile/')

    def __str__(self):
        return f"{self.username}"

class Session_date(models.Model):
    date = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.date
        
class Session_Time(models.Model):
    date = models.ForeignKey(Session_date,on_delete=models.CASCADE,null=True)
    time = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.date.date+" "+self.time

class Status(models.Model):
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.status

class Product(models.Model):
    temp = models.IntegerField(null=True)
    status  =models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    min_price = models.IntegerField(null=True)
    images = models.FileField(null=True)
    session = models.ForeignKey(Session_Time,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name