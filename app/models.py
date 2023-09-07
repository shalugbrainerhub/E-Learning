from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    role_choice=(('student', 'Student'),('instructor', 'Instructor'))
    role=models.CharField(max_length=20, choices=role_choice, default='student')
    profile_picture=models.ImageField(upload_to='profile_pics', blank=True, null=True)
     # Add a confirmation token field
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)

    # Add a boolean field to track email confirmation
    email_confirmed = models.BooleanField(default=False)


    def get_backend(self):
        return "app.backends.CustomBackend"


class Category(models.Model):
    category_choice=(('science', 'Science'),('math', 'Math'),('langauge', 'Language'),('computer', 'Computer'),('electronics', 'Electronics'))
    name=models.CharField(max_length=100, choices=category_choice, default='computer')

    def __str__(self):
        return self.name


class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    instructor=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title=models.CharField(max_length=100)
    video=models.URLField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class Enrollement(models.Model):
#     user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     course=models.ForeignKey(Course, on_delete=models.CASCADE)
#     date=models.DateTimeField(auto_now_add=True)


