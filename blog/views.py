from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 
from django import forms
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .form import ConfigurationForm




# Create your views here.





def home(request):
    
    return  render(request,'blog/acceuil.html')





@login_required
def reseau(request):
    title="Reseau"
    return  render(request,'blog/reseau.html',locals())


@login_required
def maintenance(request):
    return  render(request,'blog/maintenance.html',{'title': 'Maintenance'})


@login_required
def pooldev(request):
    return  render(request,'blog/pooldev.html',{'title': 'PoolDev'})





def article(request):

     return  render(request,'blog/article.html',{'title': 'Article'})


def listeconfig(request):
     configs=Superviser.objects.all()
     title="Reseau-Listconfig"
     return  render(request,'blog/listeconfig.html', locals())


  


def ajoutconfig(request):
     send = False
     form = ConfigurationForm(request.POST,request.FILES)
     if form.is_valid():
          form.save()
          return redirect('/reseau/listeconfig/')
     title="Reseau-AjoutConfig"
     return  render(request,'blog/ajoutconfig.html',locals())



def navbar(request):

     return  render(request,'blog/navbar.html',{'title': 'Navbar'})




def slider(request):

     return  render(request,'blog/slider.html',{'title': 'slider'})



def footer(request):

     return  render(request,'blog/footer.html',{'title': 'footer'})




def header(request):

     return  render(request,'blog/header.html',{'title': 'header'})






  



  










