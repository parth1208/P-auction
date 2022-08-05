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


