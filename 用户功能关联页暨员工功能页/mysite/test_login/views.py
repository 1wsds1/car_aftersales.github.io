# from django.shortcuts import render
from django.shortcuts import render,redirect
from test_login.models import login_msg
# Create your views here.
def login(request):
    if request.method == 'POST':
        res = {}
        if 'sub' in request.POST: #处理表单中的登录

            username = request.POST['user']
            userpwd = request.POST['userpw']
            tmp = login_msg.objects.filter(user=username).exists()

            if tmp: #若表中存在该用户名数据，则已注册

                is_reg = login_msg.objects.filter(user=username,userpw=userpwd).exists()
                if is_reg: #若查询有结果
                    return render(request,'index.html')
                else: #若查询无结果，则用户名或密码错误
                    res['rlt'] = '用户名或密码错误'
                    return render(request, 'login_in.html', res)
            else:#若表中无该用户名数据，则未注册
                res['rlt'] = '该用户名未注册，请注册后登录'
                return render(request,'login_in.html',res)
        #elif 'reg1' in request.POST: #处理表单中的注册，界面跳转
        #    return render(request,'register.html')
        else:
            pass
    return render(request,'login_in.html')




def register(request):

    if request.method == 'POST':
        res = {}
        if 'reg2' in request.POST: #处理表单中的注册
            username = request.POST['user']
            userpwd = request.POST['userpw']
            tmp = login_msg.objects.filter(user=username).exists()
            if tmp: #若存在该用户名相关数据，则用户已注册
                res['rlt'] = '该用户名已注册'
                return render(request,'login_in.html',res)
            else: #用户未注册，则向数据库中插入数据
                login_msg.objects.create(user=username,userpw=userpwd)
                res['rlt'] = '注册成功'
                return render(request,'index.html',res)
        else:
            pass
    return render(request,'login_in.html')

