from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserGame

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        

class CreateNewGame(ModelForm):
    class Meta:
        model=UserGame
        fields=['gameName','gameDescription','gameCode','gameOwnerUsername']