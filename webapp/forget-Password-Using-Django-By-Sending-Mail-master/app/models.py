from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    # email = models.EmailField(max_length=254)
    forget_token = models.CharField(max_length=1000)


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
