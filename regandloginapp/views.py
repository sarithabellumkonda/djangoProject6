from django.shortcuts import render
from .models import Reg
from django.views import View
from django.http import HttpResponse
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        return render(request,'reginput.html')
class RegInsert(View):
    def post(self,request):
        v1=request.POST['t1']
        v2 = request.POST['t2']
        v3 = request.POST['t3']
        v4 = request.POST['t4']
        v5 = request.POST['t5']
        v6 = request.POST['t6']
        v7 = int(request.POST['t7'])
        r=Reg(username=v1,password=v2,conf_password=v3,first_name=v4,last_name=v5,
              emailid=v6,mobileno=v7)
        r.save()
        return HttpResponse("Registration Successfull")
class LoginInput(View):
    def get(self,request):
        return render(request,'logininput.html')
class LoginVerf(View):
    def post(self,request):
        user = request.POST['p1']
        passw = request.POST['p2']
        dbuser= Reg.objects.filter(username =user, password=passw)
        if not dbuser:
            return HttpResponse("Login Failed")
        else:
            return HttpResponse("Login Successful")