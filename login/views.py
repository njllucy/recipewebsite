from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import mysql.connector as sql
def error(request):
    return render(request,'base/error.html')
def welcome(request):
    return render(request,'base/welcome.html')
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'base/error.html')
        else:
            return render(request,"base/welcome.html")

    return render(request,'base/login_page.html')