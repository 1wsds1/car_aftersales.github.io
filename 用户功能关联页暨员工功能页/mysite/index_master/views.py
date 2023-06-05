from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render,HttpResponse,redirect,reverse
# Create your views here.


def login(request):

    return render(request,'index.html')

def index(request):
    print("进入index")
    return redirect(reverse('login'))


