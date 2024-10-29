"""
URL configuration for EmployeeRecordMgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name='index'),
    path('registration', registration ,name='registration'),
    path('login', login_auth ,name='login'),
    path('emphome', emphome ,name='emphome'),
    path('profile', profile ,name='profile'),
    path('emplogout', emplogout ,name='emplogout'),
    path('my_experience', my_experience,name='my_experience'),
    path('my_education', my_education,name='my_education'),
    path('edit_experience', edit_experience,name='edit_experience'),
    path('edit_education', edit_education,name='edit_education'),
    path('change_pass', change_pass,name='change_pass'),
    path('admin_login', admin_login,name='admin_login'),
    path('admin_home', admin_home ,name='admin_home'),
    path('admin_pass', admin_pass,name='admin_pass'),
    path('admin_employee', admin_employee,name='admin_employee'),
    path('admin_edit_emp/<str:pname>/',admin_edit_emp,name='admin_edit_emp'),
    path('admin_edit_edu/<str:pname>/',admin_edit_edu,name='admin_edit_edu'),
    path('admin_edit_exp/<str:pname>/',admin_edit_exp,name='admin_edit_exp'),
]
