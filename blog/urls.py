from django.urls import path
from . import views
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [

    path('', views.home, name='acceuil'),
    path('reseau/', views.reseau, name='reseau'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('pooldev/', views.pooldev, name='pooldev'),
    path('article/', views.article, name='article'),
    path('reseau/listeconfig/', views.listeconfig, name='listeconfig'),
    path('reseau/ajoutconfig/', views.ajoutconfig, name='ajoutconfig'),
    path('navbar/', views.navbar, name='navbar'),
    path('slider/', views.slider, name='slider'),
    path('footer/', views.footer, name='footer'),
    path('header/', views.header, name='header'),

    

]


