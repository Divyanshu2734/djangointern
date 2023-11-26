from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import uploader

def signup(request):
    if request.method=='POST':
        name=request.POST['fname']
        lname=request.POST['lname']
        add=request.POST['address']
        user_img=request.POST['uimg']
        uemail=request.POST['email']
        upass=request.POST['password']
        ucpass=request.POST['confpassword']
        u_types=request.POST['utypes']
        if upass!=ucpass:
            messages.warning(request,"password is incorrect")
            return redirect("/signup/")
        person=User.objects.create_user(uemail,uemail,upass)
        mydetails=uploader(uploader_name=name,uploader_last=lname,uploader_add=add,uploader_type=u_types,uploader_img=user_img)
        # person.fristname=name
        # person.lastname=lname
        # person.uadd=add
        # person.holder=u_types
        mydetails.save()
        person.save()
        messages.success(request,"your signup is done")
        return redirect("/login/")
    return render(request, "signup.html")

def signin(request):
    if request.method=='POST':
        user_name=request.POST['email']
        user_pass=request.POST['password']
        holder=request.POST['user_type']
        myuser=authenticate(username=user_name,password=user_pass)

        if myuser is not None and holder=='doctor' :
         login(request,myuser)
         return redirect("/doctor/")
        elif myuser is not None and holder=='patient':
         login(request,myuser)
         return redirect("/patient/")
        
    return render(request, "login.html")

def signout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect("/signup/")


def doctor(request):
    return render(request, "doctordetails.html")

def patient(request):
    return render(request, "patientdetails.html")

def base(request):
    return render(request, "base2.html")


