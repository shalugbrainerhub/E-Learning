from imaplib import _Authenticator
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=['username','email','role','password']




class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser



class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)

    
class LectureForm(forms.ModelForm):
    class Meta:
        model=Lecture
        fields='__all__'

        

