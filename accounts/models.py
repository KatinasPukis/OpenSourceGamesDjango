from django.db import models
# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)


class UserGame(models.Model):
    gameName=models.CharField(max_length=200,null=True)
    gameDescription=models.CharField(max_length=1000,null=True)
    gameCode=models.CharField(max_length=100000,null=True)
    gameOwnerUsername=models.CharField(max_length=200,null=True)


class NewsClass(models.Model):
    headline=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=200,null=True)
    text=models.CharField(max_length=200,null=True) 