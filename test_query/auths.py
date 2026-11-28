from django.shortcuts import render, redirect
from .models import User
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

#--------> Register Page 
def register_page(request):
    form = RegisterFrom(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('test_query:login')

    context = {
        'form': form,
        'page_title': 'Register Page',
        'btn' : 'Register'
    }
    return render(request, 'form.html', context)



#--------> Login Page
def login_page(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        if user:
            login(request, user)
            return redirect('test_query:data')

    context = {
        'form': form,
        'page_title': 'Login Page',
        'btn' : 'Login'
    }
    return render(request, 'form.html', context)



#--------> Logout Page
def logout_page(request):
    logout(request)
    return redirect('test_query:login')