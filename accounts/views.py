from django.shortcuts import redirect, render

from accounts.models import Customer, UserGame, NewsClass
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateNewNews, CreateUserForm, CreateNewGame
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    news= NewsClass.objects.all()
    return render(request,'accounts/index.html',{'news':news})

def news(request):

    news= NewsClass.objects.all()
    return render(request,'accounts/news.html',{'news':news})

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

def uploadGame(request):
    form=CreateNewGame()
    uloggedinuser=request.user.username
    form = CreateNewGame(initial={'gameOwnerUsername': uloggedinuser})
    if request.method=='POST':
        form=CreateNewGame(request.POST)
        print(request.POST)
        
        if form.is_valid():
            print('pasol naxui')
            form.save()
            return redirect('games')
    context={'form':form}

    return render(request,'accounts/uploadGame.html',context)


def newsPage(request,pk):
    news=NewsClass.objects.get(id=pk)
    context={'news':news}
    return render(request,'accounts/newsPage.html',context)

def uploadNews(request):
    form=CreateNewNews()
 
    if request.method=='POST':
        form=CreateNewNews(request.POST)
        print(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('news')
    context={'form':form}
    return render(request,'accounts/uploadNews.html',context)


    
