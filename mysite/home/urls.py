"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .import views
from django.contrib import admin
from django.urls import path
app_name='home'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.mysiteinfo, name='mysiteinfo'),
    path('loginpage', views.LoginPage, name='loginpage'),
    path('userLogout', views.UserLogout, name='userLogout'),
    path('register', views.Register, name='register'),
    path('blogpage',views.blogpage,name='blogpage'),
    path('create_blog', views.create_blog, name='create_blog'),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),

    path('dashbord', views.dashbord, name='dashbord'),
    path('details/<int:sid>', views.details, name='details'),
    path('delete/<int:did>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),

    path('task_list',views.task_list,name='task_list'),
    path('task_detail/<int:dtid>', views.task_detail, name='task_detail'),
    path('apply',views.apply,name='apply'),


]
