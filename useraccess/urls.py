from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup', views.signUp, name= "signup"),
    path('login', views.loginUser, name= "login"),
    path('logout', views.logoutUser, name= "logout"),
]