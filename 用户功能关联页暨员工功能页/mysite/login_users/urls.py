'''
from login_users.views import logout,logon,login
from django.urls import path

urlpatterns = [
    path('login/',login,name='login'),
    path('logon/',logon,name='logon'),
    path('logout/', logout, name='logout'),
]'''

from login_users.views import login_in
from django.urls import path

urlpatterns = [
    path('',login_in,name='login_in'),

]


