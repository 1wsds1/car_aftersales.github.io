"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from index_master.views import index
from login_users.views import index_login
import test_login.views as minelogin_views


urlpatterns = [
    path("admin/", admin.site.urls),

    path('login/', minelogin_views.login),
    path('register/', minelogin_views.register),


]

'''
    path("index_master/", include("index_master.urls")),
    path('', index, name='index'),

    path('login_users/',include('login_users.urls')),
    path('login/',index_login,name='index_login')
'''
