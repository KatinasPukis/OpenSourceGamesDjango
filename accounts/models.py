from django.db import models 
from django.contrib.auth.models import User


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
    image = models.ImageField(null=True, blank=True)
    gameOwnerUsername=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.gameName


class NewsClass(models.Model):
    headline=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=200,null=True)
    text=models.CharField(max_length=200,null=True) 
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.headline

class Comment(models.Model):
    userid=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    newsid=models.ForeignKey(NewsClass, null=True, on_delete=models.SET_NULL)
    commentText=models.CharField(max_length=10000,null=True)
    def __str__(self):
        return self.commentText
    
     
