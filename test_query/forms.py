from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']