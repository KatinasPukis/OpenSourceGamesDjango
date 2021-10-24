from django.shortcuts import redirect, render

from accounts.models import Customer, UserGame
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    customer=Customer.objects.all()
    return render(request,'accounts/index.html')

def news(request):
    return render(request,'accounts/news.html')

def register(request):
    form= CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, 'Paskyra sukurta '+ username)
            return redirect('login')

    context={'form':form}
    return render(request,'accounts/register.html',context)

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Slapyvardis arba slaptazodis neteisingas!')
    context={}
    return render(request,'accounts/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def games(request):

    userGame= UserGame.objects.all()
    return render(request,'accounts/games.html',{'userGame':userGame})

def gamesPage(request,pk):

    userGame= UserGame.objects.get(id=pk)
    context={'userGame':userGame}
    return render(request,'accounts/gamesPage.html',context)