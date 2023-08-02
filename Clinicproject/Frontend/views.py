from django.shortcuts import render,redirect
from Clinicapp.models import departmentdb,doctorsdb
from Frontend.models import appointmentdb,regdb

# Create your views here.
def homepage(request):
    data = departmentdb.objects.all()
    return render(request,"home.html",{'data':data})


def deppage(request):
    data = departmentdb.objects.all()
    return render(request, "dep_page.html", {'data': data})

def docpage(request):
    data = departmentdb.objects.all()
    products= doctorsdb.objects.all()
    return render(request,"doctors_page.html",{'data':data,'products':products})

def appointmentpage(request):
    data = departmentdb.objects.all()
    return render(request, "appointment.html", {'data': data})


def saveappointment(request):
    if request.method == "POST":
            na = request.POST.get('name')
            em = request.POST.get('email')
            mb = request.POST.get('mobile')
            de = request.POST.get('department')
            dr = request.POST.get('doctor')
            de = request.POST.get('datetime')
            pl = request.POST.get('place')
            obj = appointmentdb(Name=na, Email=em,Mobile=mb,Department=de,Doctor=dr,Datetime=dt,Place=pl)
            obj.save()
            return redirect(appointmentpage)


def signuppage(request):
    return render(request,"register.html")

def savesignup(request):
    if request.method=="POST":
        una=request.POST.get('username')
        em = request.POST.get('email')
        ps=request.POST.get('password')
        cps=request.POST.get('confirmpassword')
        obj=regdb(Username=una,Email=em,Password=ps,Confirm_password=cps)
        obj.save()
        return redirect(signuppage)
def userlogin(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if regdb.objects.filter(Username=username_r,Password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            return redirect(homepage)
        else:
            return redirect(signuppage)
    return redirect(signuppage)
def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('signuppage')