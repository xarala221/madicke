from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import login as auth_login
from .models import *
from django.contrib.auth import logout
from django.shortcuts import redirect



# Create your views here.





def login(request):


    title = 'login'
    return  render(request,'users/login.html',locals())



def signup(request):
    username_error = password_error = password_length_error = name_error = False 
    title = 'signup'

    if(request.POST):
        email = request.POST['email']
        password = request.POST['password']
        repass = request.POST['repass']
        name = request.POST["name"]
        if (len(name) < 5):
            name_error = True
        if (len(password) < 6):
            password_length_error = name_error = True
        elif password != repass:
            password_error = True
        else:
            users = User.objects.all()
            for user in users:
                if user.username == email:
                    username_error = True
            if not username_error:
                new_user = User.objects.create_user(email, email, password)
                # new_user.name = name
                user = Users()
                user.user = new_user
                # user.name = name
                user.save()

                #new_user = authenticate(email=email, password=password)
                #dj_login(request, new_user)

                return redirect('users:login')
        
    return  render(request,'users/signup.html',{'title': 'inscription'})



def login(request):
    username_error = password_error = error = False
  
    if request.POST:
        email = request.POST["email"]
        password = request.POST["password"]

        if (len(password) < 6):
            password_error = True

        users = User.objects.all()
        
        user = authenticate(username=email, password=password)
        if user is not None:
            dj_login(request, user)
            error = True
            if request.GET.get('next', False):
                return redirect(request.GET['next'])
            else:
                return redirect("/")
        else:
            error = True
    return render(request, 'users/login.html', {'title': 'connexion'})



def deconnect(request):
   logout(request)
   return redirect('/')



def profile(request):
    title = 'profile'
    return  render(request,'users/profile.html',locals())
