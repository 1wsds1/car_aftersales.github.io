from django.shortcuts import render,HttpResponse,redirect,reverse
#from models import Account
# Create your views here.
'''
def login(request):
    if request.method == 'POST':
        print("进入页面")
        email = request.POST['username']
        password = request.POST['password']
        corr_email = Account.objects.filter(email=email).first()
        print("获取到信息")
        if email == corr_email.email and password == corr_email.password:
            print('登录成功')
            return HttpResponse('登录成功')
    return render(request, './templates/log_in.html')

def logon(request):
    return HttpResponse('注册页面')

def logout(request):
    return HttpResponse('退出')

def index_login(request):
    return redirect(reverse('login'))
'''
from django.shortcuts import render,HttpResponse,redirect,reverse
# Create your views here.


def login_in(request):

    return render(request,'login_in.html')

def index_login(request):
    return redirect(reverse('login_in'))
