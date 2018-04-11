# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegister
#from django.http import HttpResponse

# Create your views here.
def index(request):
    data=request.POST
    message=None 
    if request.method == 'POST':
        form=UserRegister(data)
        if form.is_valid():
            user=User.objects.filter(email=data['email'])
            try:
                if not user:
                    new_user=User(email=data['email'], password=data['password'])
                    new_user.save()
                    message = 'Successfully logged in'
                    return redirect('login')
                else:
                    message = 'User already exists'
            except:
                message='Errorrrr'
    else:
        form=UserRegister()
      
    context={'form':form, 'messages':message}
    return render(request, 'users/index.html', context)

def login(request):
    data=request.POST
    message=None 
    if request.method == 'POST':
        form=UserRegister(data)
        if form.is_valid():
            user=User.objects.filter(email=data['email'])
            try:
                if users:
                    message = 'Successfully logged in'
                    return redirect('dashboard')
            except:
                message = 'user already exists'
    else:
        message='Problems'
    form=UserRegister()
    context={'form':form, 'messages':message}
    return render(request, 'users/login.html', context)
