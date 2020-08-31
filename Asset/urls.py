"""Asset URL Configuration

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
from django.contrib import admin
from django.urls import path
from asset_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name='Home'),
    path('', Index, name='home'),
    path('admin_login', Login, name='login'),
    path('logout/', Logout_admin, name='logout'),
    path('view_laptop/', View_Laptop, name='view_laptop'),
    path('add_laptop/', Add_Laptop, name='add_laptop'),
    path('delete_laptop(?p<int:pid>)', Delete_Laptop, name = 'delete_laptop'),
    path('view_desktop/', View_Desktop, name='view_desktop'),
    path('add_desktop/', Add_Desktop, name='add_desktop'),
    path('delete_desktop(?p<int:pid>)', Delete_Desktop, name = 'delete_desktop'),
    path('edit_laptop(?p<int:pid>)', Edit_Laptop, name = 'edit_laptop'),

]
