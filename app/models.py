from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    role_choice=(('student', 'Student'),('instructor', 'Instructor'))
    role=models.CharField(max_length=20, choices=role_choice, default='student')
    profile_picture=models.ImageField(upload_to='profile_pics', blank=True, null=True)