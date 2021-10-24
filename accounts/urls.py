from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('games/', views.games, name='games'),
    path('gamesPage/<str:pk>/', views.gamesPage, name='gamesPage'),
    path('uploadGame/', views.uploadGame, name='uploadGame'),
    path('newsPage/<str:pk>/', views.newsPage, name='newsPage'),
    path('uploadNews', views.uploadNews, name='uploadNews'),
]
