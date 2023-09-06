
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login_view, name='login'),
    path('confirm/<uuid:token>/', views.confirm_email, name='confirm_email'),
    path('course', views.course, name='course'),
    path('instructor_dashboard', views.instructor_dashboard, name='instructor_dashboard'),
    path('update_course/<int:pk>', views.update_course, name='update_course'),
    path('delete_course/<int:pk>', views.delete_course, name='delete_course')
    
]
