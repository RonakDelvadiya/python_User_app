from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re


def home(request):
    user = request.user.username
    return render(request, 'home.html',{'name':user})


def logout_views(request):
    logout(request)
    return render(request,'login.html',{}) 


def register(request):
    if request.method == 'POST':
        user_details=request.POST
        rpwd = user_details.get('rpassword')
        pwd = user_details.get('password')
        fname = user_details.get('fname')
        lname = user_details.get('lname')
        email = user_details.get('email')
        uname = user_details.get('username')
        queryset = User.objects.all().filter(username=uname)
        pass1 = pwd
        
        if queryset:
            return render(request,'registration.html',{'usererror': 'username already exist'})
        else:
            if re.match(r"^(?=.*\d).{6,12}$", pass1):
                if (rpwd == pwd):
                    user=User.objects.create_user(uname,email,pwd)
                    user.save()
                    return HttpResponseRedirect('/account/login_views/')
                else:
                    return render(request,'registration.html',{'error': 'Your password and conform password both are not match'})
            else:
                return render(request,'registration.html',{'passerror': 'Your  password must be between 6 and 12 digits long and include at least one numeric digit.'})
    return render(request,'registration.html')
   

def login_views(request):
    if request.method == 'POST':
        form_data=request.POST
        uname=form_data.get('username')
        pwd=form_data.get('password')
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/account/home/')
        else:
            return render(request, 'login.html',{'error':'your username and password are invalid'})
    return render(request,'login.html',{})
