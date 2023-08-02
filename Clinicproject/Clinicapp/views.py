from django.shortcuts import render,redirect, get_object_or_404
from .models import Admin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Clinicapp.models import departmentdb,doctorsdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin_list.html', {'admins': admins})

def create_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = Admin(name=name, email=email, password=password)
        admin.save()
        return redirect('admin_list')

    return render(request, 'create_admin.html')

def edit_admin(request, admin_id):
    admin = get_object_or_404(Admin, id=admin_id)

    if request.method == 'POST':
        admin.name = request.POST.get('name')
        admin.email = request.POST.get('email')
        admin.password = request.POST.get('password')
        admin.save()
        return redirect('admin_list')

    return render(request, 'edit_admin.html', {'admin': admin})




def delete_admin(request, admin_id):
    admin = get_object_or_404(Admin, id=admin_id)

    if request.method == 'POST':
        admin.delete()
        return redirect('admin_list')

    return render(request, 'delete_admin.html', {'admin': admin})






def loginpage(request):
    return render(request,"admin_login.html")



def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)


def indexpage(request):
    return render(request, "index.html")


def departmentpage(request):
    return render(request, "adddepartment.html")

def savedepartment(request):
    if request.method == "POST":
        na = request.POST.get('name')
        img = request.FILES['image']
        dsp = request.POST.get('description')
        obj = departmentdb(Name=na, Image=img, Description=dsp)
        obj.save()
        return redirect(departmentpage)


def displaydepartment(request):
    data = departmentdb.objects.all()
    return render(request, "display_department.html", {'data': data})


def editdepartment(request, dataid):
    data = departmentdb.objects.get(id=dataid)
    print(data)
    return render(request, "edit_category.html", {'data': data})


def updatedepartment(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        dsp = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = departmentdb.objects.get(id=dataid).Image
        departmentdb.objects.filter(id=dataid).update(Name=na, Description=dsp, Image=file)
        return redirect(displaydepartment)


def deletedepartment(request, dataid):
    data = departmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydepartment)

def doctorspage(request):
    data = departmentdb.objects.all()
    return render(request, "adddoctors.html", {'data': data})

def doctorssave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ct = request.POST.get('category')
        qt = request.POST.get('qualification')
        img = request.FILES['image']
        obj = doctorsdb(Name=na,Category=ct, Image=img, Qualification=qt)
        obj.save()
        return redirect(doctorspage)

def displaydoctors(request):
    data = doctorsdb.objects.all()
    return render(request, "display_doctors.html", {'data': data})

def editdoctors(request, dataid):
    data = doctorsdb.objects.get(id=dataid)
    da = doctorsdb.objects.all()
    return render(request, "edit_doctors.html", {'data': data, 'da': da})


def updatedoctors(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        ct = request.POST.get('category')
        qt = request.POST.get('qualification')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = doctorsdb.objects.get(id=dataid).Image
        doctorsdb.objects.filter(id=dataid).update(Name=na, Category=ct,Image=file,Qualification=qt)
        return redirect(displaydoctors)


def deletedoctors(request, dataid):
    data = doctorsdb.objects.filter(id=dataid)
    data.delete()
    return redirect(doctorspage)





