from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    is_Budder=models.BooleanField('Is Bidder',default=False)
    is_seller=models.BooleanField('Is seller',default=False)
    image = models.ImageField(upload_to='Profile/')

    def __str__(self):
        return f"{self.username}"

class Session_date(models.Model):
    date = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.date


class Status(models.Model):
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.status

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status  =models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    min_price = models.IntegerField(null=True)
    images = models.FileField(null=True)
    from_city=models.CharField(max_length=100,null=True)
    to_city=models.CharField(max_length=100,null=True)
    weight=models.IntegerField(null=True)
    distance=models.IntegerField(null=True)
    parcel_type=models.CharField(max_length=100,null=True)
    session = models.ForeignKey(Session_date,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name 
         

class Aucted_Product(models.Model):
    winner = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.user.username+ " " + self.product.name
