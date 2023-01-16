from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt

import datetime
# Create your views here.

def h_fun(request):
    return HttpResponse("This is HR Page")

# def now(request):
#     now=datetime.datetime.now()
#     msg=f'Today is {now}'
#     return HttpResponse(msg)


# def image(request):
#     img=open('C:\\Users\\DELL\\Desktop\\cat.jpg','rb')
#     return FileResponse(img)

def home(request):
    return render(request,'home.html',{'name':'Sandip'})


def add(request):
    val1=int(request.GET["num1"])
    val2=int(request.GET["num2"])
    res=val1+val2
    return render(request,'result.html',{'result':res})


def sub(request):
    val1=int(request.GET["num1"])
    val2=int(request.GET["num2"])
    res=val1-val2
    return render(request,'result.html',{'result2':res})

# @csrf_exempt
# def add(request):
#     val1=int(request.POST["num1"])
#     val2=int(request.POST["num2"])
#     res=val1+val2
#     return render(request,'result.html',{'result':res})