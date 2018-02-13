from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re


# Create your views here.


def home(request):
    user = request.user.username
    return render(request, 'home.html',{'name':user})
    
def logout_views(request):
    logout(request)
    return render(request,'login.html',{}) 


def register(request):
    if request.method == 'POST':
        print "in post"
        user_details=request.POST
        rpwd = user_details.get('rpassword')
        pwd = user_details.get('password')
        fname = user_details.get('fname')
        lname = user_details.get('lname')
        email = user_details.get('email')
        uname = user_details.get('username')
        queryset = User.objects.all().filter(username=uname)
        pass1 = pwd
        #print queryset
        
        if queryset:
            #print "if"
            return render(request,'registration.html',{'usererror': 'username already exist'})
        else:
            #print "else"
            if re.match(r"^(?=.*\d).{6,12}$", pass1):
                print "match"
                if (rpwd == pwd):
                    user=User.objects.create_user(uname,email,pwd)
                    user.save()
                #return render(request,'login.html',{})
                    return HttpResponseRedirect('/account/login_views/')
                else:
                    return render(request,'registration.html',{'error': 'Your password and conform password both are not match'})
            else:
                print "not match"
                return render(request,'registration.html',{'passerror': 'Your  password must be between 6 and 12 digits long and include at least one numeric digit.'})
    return render(request,'registration.html')
   

def login_views(request):
    print "in login"
    print request.method
    if request.method == 'POST':

        print "from log in post"
        form_data=request.POST
        uname=form_data.get('username')
        pwd=form_data.get('password')
        # queryset = User.objects.all().filter(username=uname).filter (password=pwd)
        # print queryset
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/account/home/')
        else:
            return render(request, 'login.html',{'error':'your username and password are invalid'})
    print "from log out of post"
    return render(request,'login.html',{})