#from django.db import models

# Create your models here.
from django.db import models

class login_msg(models.Model):
    user = models.CharField(max_length=30) #用户名
    userpw = models.CharField(max_length=128) #用户密码
