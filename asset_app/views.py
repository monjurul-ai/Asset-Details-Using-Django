from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.
from .models import *


def Home(request):
    return render(request,'home.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    laptop = Laptop.objects.all()
    desktop = Desktop.objects.all()

    l = 0;
    d = 0;

    for i in laptop:
        l+=1

    for i in desktop:
        d+=1
    d1 = {'l':l, 'd':d}
    return render(request,'index.html',d1)


def Login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')



def View_Laptop(request):
    if not request.user.is_staff:
        return redirect('login')
    lap = Laptop.objects.all()
    l = {'lap':lap}
    return render(request,'view_laptop.html',l)


def Add_Laptop(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':

        ui = request.POST['UserId']
        fn = request.POST['FullName']
        e = request.POST['Email']
        bd = request.POST['Brand']
        rm = request.POST['Ram']
        hd = request.POST['HardDisk']
        s = request.POST['SSD']
        bt = request.POST['Battery']
        cr = request.POST['Charger']
        pm = request.POST['Processor_Model']
        mc = request.POST['MacAddress']
        d1 = request.POST['date1']
        t1 = request.POST['time1']


        try:
           Laptop.objects.create(UserId=ui, FullName=fn, Email=e, Brand=bd, RAM=rm, HardDisk=hd, SSD=s, Battery=bt, Processor_Model=pm, Charger=cr, MacAddress=mc, date1=d1, time1=t1)
           error = "no"

        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_laptop.html',d)

def Delete_Laptop(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    laptop = Laptop.objects.get(id = pid)
    laptop.delete()
    return redirect('view_laptop')




def Edit_Laptop(request,pid):
    laptop = Laptop.objects.get(id = pid)
    l = {'laptop':laptop}
    laptop.save()

    #post = get_object_or_404(pid=pid)
    #if request.method == "POST":
        #form = Post.
    #if not request.user.is_staff:
        #return redirect('login')
    #laptop = Laptop.objects.get(id = pid)
    return render(request,'edit_laptop.html',l)



def View_Desktop(request):
    if not request.user.is_staff:
        return redirect('login')
    des = Desktop.objects.all()
    l = {'des':des}
    return render(request,'view_desktop.html',l)


def Add_Desktop(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method =='POST':
        ui = request.POST['UserId']
        fn = request.POST['FullName']
        e = request.POST['Email']
        bd = request.POST['Brand']
        rm = request.POST['Ram']
        hd = request.POST['HardDisk']
        s = request.POST['SSD']
        bt = request.POST['Battery']
        cr = request.POST['Charger']
        pm = request.POST['Processor_Model']
        mc = request.POST['MacAddress']
        d1 = request.POST['date1']
        t1 = request.POST['time1']


        try:
           Desktop.objects.create(UserId=ui,FullName=fn,Email=e,Brand=bd,RAM=rm,HardDisk=hd,SSD=s,Battery=bt,Processor_Model=pm,Charger=cr,MacAddress=mc,date1=d1,time1=t1)
           error = "no"

        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_desktop.html',d)

def Delete_Desktop(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    desktop = Desktop.objects.get(id = pid)
    desktop.delete()
    return redirect('view_desktop')
