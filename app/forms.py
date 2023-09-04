from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=['username','email','password','role', 'profile_picture']



# class LoginForm(AuthenticationForm):
#     pass
    