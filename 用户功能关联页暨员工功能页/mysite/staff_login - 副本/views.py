# from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        res = {}
        if 'sub' in request.POST: #处理表单中的登录

            username = request.POST['user']
            userpwd = request.POST['userpw']
            

            if username == 'admin1': #若表中存在该用户名数据，则已注册
                if userpwd =="123456":
                
                    return render(request,'index_staff.html')
                else: #若查询无结果，则用户名或密码错误
                    res['rlt'] = '用户名或密码错误'
                    return render(request, 'signup_staff.html', res)
            if username == 'admin2': #若表中存在该用户名数据，则已注册
                if userpwd =="159846":
                
                    return render(request,'index_staff.html')
                else: #若查询无结果，则用户名或密码错误
                    res['rlt'] = '用户名或密码错误'
                    return render(request, 'signup_staff.html', res)
            else:#若表中无该用户名数据，则未注册
                res['rlt'] = '用户名或密码错误'
                return render(request, 'signup_staff', res)
        #elif 'reg1' in request.POST: #处理表单中的注册，界面跳转
        #    return render(request,'register.html')
        else:
            pass
    return render(request,'signup_staff.html')



