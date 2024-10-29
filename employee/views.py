from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.
from .models import *


def index(request):
    return render(request,'index.html')

def registration(request):
    error=""
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        ec=request.POST['ecode']
        em=request.POST['email']
        pwd=request.POST['passwd']
        try:
            user= User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            employeedetail.objects.create(user=user,empcode=ec)
            employee_experience.objects.create(user=user)
            employee_education.objects.create(user=user)
            error="no"
        except:
            error="yes"
        
    return render(request,'registration.html',locals())
def login_auth(request):
    error=""
    if request.method=='POST':
        u=request.POST['emailid']
        p=request.POST['passwd']
        user= authenticate(username=u,password=p)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("emphome")
            else:
                error="yes"
        error="yes"
        
    return render(request,'login.html',locals())

def emphome(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request,'emphome.html',locals())


def emplogout(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logout(request)
    return render(request,"index.html")

def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user=request.user
    employee=employeedetail.objects.get(user=user)
    error=""
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        ec=request.POST['ecode']
        d=request.POST['department']
        de=request.POST['designation']
        jd=request.POST['jdate']
        gen=request.POST['gender']
        con=request.POST['contact']
        
        
        employee.user.first_name=fn
        employee.user.last_name=ln
        employee.empcode=ec
        employee.gender=gen
        employee.dept=d
        employee.contact=con
        employee.designation=de
        if jd:
            employee.joingdate=jd
        
        
        try:
            employee.save()
            employee.user.save()
            error="no"
        except:
            error="yes"
        print(error)

        
    return render(request,'profile.html',locals())


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user =request.user
    ex=employee_experience.objects.get(user=user)
    return render(request,'my_experience.html',locals())

def my_education(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user =request.user
    ex=employee_education.objects.get(user=user)
    return render(request,'my_education.html',locals())

def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user =request.user
    ex=employee_experience.objects.get(user=user)
    error=""
    if request.method=="POST":
        c1n=request.POST['c1n']
        c1d=request.POST['c1d']
        c1dur=request.POST['c1dur']
        c1s=request.POST['c1s']
        c2n=request.POST['c2n']
        c2d=request.POST['c2d']
        c2dur=request.POST['c2dur']
        c2s=request.POST['c2s']
        c3n=request.POST['c3n']
        c3d=request.POST['c3d']
        c3dur=request.POST['c3dur']
        c3s=request.POST['c3s']
        
        
        ex.company1=c1n
        ex.company1_des=c1d
        ex.company1_salary=c1s
        ex.company1dur=c1dur
        ex.company2=c2n
        ex.company2_des=c2d
        ex.company2_salary=c2s
        ex.company2dur=c2dur
        ex.company3=c3n
        ex.company3_des=c3d
        ex.company3_salary=c3s
        ex.company3dur=c3dur
        
        
        try:
            ex.save()
            error="no"
        except:
            error="yes"
    return render(request,'e_experience.html',locals())


def edit_education(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user =request.user
    ex=employee_education.objects.get(user=user)
    error=""
    if request.method=="POST":
        e1n=request.POST['e1n']
        e1c=request.POST['e1c']
        e1p=request.POST['e1p']
        e1y=request.POST['e1y']
        
        e2n=request.POST['e2n']
        e2c=request.POST['e2c']
        e2p=request.POST['e2p']
        e2y=request.POST['e2y']
        
        e3n=request.POST['e3n']
        e3c=request.POST['e3c']
        e3p=request.POST['e3p']
        e3y=request.POST['e3y']
        
        e4n=request.POST['e4n']
        e4c=request.POST['e4c']
        e4p=request.POST['e4p']
        e4y=request.POST['e4y']
        
        
        ex.epg=e1n
        ex.colpg=e1c
        ex.perpg=e1p
        ex.ypg=e1y
        
        ex.eg=e2n
        ex.colg=e2c
        ex.perg=e2p
        ex.yg=e2y
        
        ex.ess=e3n
        ex.colss=e3c
        ex.perss=e3p
        ex.yss=e3y
        
        ex.eh=e4n
        ex.colh=e4c
        ex.perh=e4p
        ex.yh=e4y
        
        
        try:
            ex.save()
            error="no"
        except:
            error="yes"
    return render(request,'e_education.html',locals())


def change_pass(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    error=""
    if request.method=="POST":
        user =request.user
        curp=request.POST['currpasswd']
        np=request.POST['passwd'] 
        try:
            if user.check_password(curp):
                user.set_password(np)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    return render(request,'change_pass.html',locals())

def admin_login(request):
    error=""
    if request.method=='POST':
        u=request.POST['emailid']
        p=request.POST['passwd']
        user= authenticate(username=u,password=p)
        if user.is_staff:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("admin_home")
            else:
                error="yes"
        error="yes"
        
    return render(request,'admin_login.html',locals())
def admin_home(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    return render(request,'admin_home.html',locals())


def admin_pass(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    
    error=""
    if request.method=="POST":
        user =request.user
        curp=request.POST['currpasswd']
        np=request.POST['passwd'] 
        try:
            if user.check_password(curp):
                user.set_password(np)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    return render(request,'admin_pass.html',locals())
def admin_employee(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    user=request.user
    employee=employeedetail.objects.all()
    error=""   
    return render(request,'admin_employee.html',locals())



def admin_edit_emp(request, pname):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    user = get_object_or_404(User, username=pname)
    employee = get_object_or_404(employeedetail, user=user)

    error=""
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        ec=request.POST['ecode']
        d=request.POST['department']
        de=request.POST['designation']
        jd=request.POST['jdate']
        gen=request.POST['gender']
        con=request.POST['contact']
        
        
        employee.user.first_name=fn
        employee.user.last_name=ln
        employee.empcode=ec
        employee.gender=gen
        employee.dept=d
        employee.contact=con
        employee.designation=de
        if jd:
            employee.joingdate=jd
        
        
        try:
            employee.save()
            employee.user.save()
            error="no"
        except:
            error="yes"
       

    return render(request, 'admin_edit_emp.html', locals())



def admin_edit_edu(request, pname):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    user = get_object_or_404(User, username=pname)
    ex = get_object_or_404(employee_education, user=user)

    error=""
    if request.method=="POST":
        e1n=request.POST['e1n']
        e1c=request.POST['e1c']
        e1p=request.POST['e1p']
        e1y=request.POST['e1y']
        
        e2n=request.POST['e2n']
        e2c=request.POST['e2c']
        e2p=request.POST['e2p']
        e2y=request.POST['e2y']
        
        e3n=request.POST['e3n']
        e3c=request.POST['e3c']
        e3p=request.POST['e3p']
        e3y=request.POST['e3y']
        
        e4n=request.POST['e4n']
        e4c=request.POST['e4c']
        e4p=request.POST['e4p']
        e4y=request.POST['e4y']
        
        
        ex.epg=e1n
        ex.colpg=e1c
        ex.perpg=e1p
        ex.ypg=e1y
        
        ex.eg=e2n
        ex.colg=e2c
        ex.perg=e2p
        ex.yg=e2y
        
        ex.ess=e3n
        ex.colss=e3c
        ex.perss=e3p
        ex.yss=e3y
        
        ex.eh=e4n
        ex.colh=e4c
        ex.perh=e4p
        ex.yh=e4y
        
        
        try:
            ex.save()
            error="no"
        except:
            error="yes"
       

    return render(request, 'admin_edit_edu.html', locals())

def admin_edit_exp(request, pname):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    user = get_object_or_404(User, username=pname)
    ex = get_object_or_404(employee_experience, user=user)

    error=""
    if request.method=="POST":
        c1n=request.POST['c1n']
        c1d=request.POST['c1d']
        c1dur=request.POST['c1dur']
        c1s=request.POST['c1s']
        c2n=request.POST['c2n']
        c2d=request.POST['c2d']
        c2dur=request.POST['c2dur']
        c2s=request.POST['c2s']
        c3n=request.POST['c3n']
        c3d=request.POST['c3d']
        c3dur=request.POST['c3dur']
        c3s=request.POST['c3s']
        
        
        ex.company1=c1n
        ex.company1_des=c1d
        ex.company1_salary=c1s
        ex.company1dur=c1dur
        ex.company2=c2n
        ex.company2_des=c2d
        ex.company2_salary=c2s
        ex.company2dur=c2dur
        ex.company3=c3n
        ex.company3_des=c3d
        ex.company3_salary=c3s
        ex.company3dur=c3dur
        
        
        try:
            ex.save()
            error="no"
        except:
            error="yes"

    return render(request, 'admin_edit_exp.html', locals())
