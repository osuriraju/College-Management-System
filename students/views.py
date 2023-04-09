from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from .forms import ClassForm, FacultyForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(User, username=username, password=password)
        if user is not None:
            messages.info(request, 'Successfully logged in')
            return redirect('/index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email, password=password)
            user.save()
            messages.info(request, 'Successfully registered')
            return redirect('/')
        else:
            messages.info(request, "Password didn't match")
            return render(request, 'register.html')

    return render(request, 'register.html')



def index(request):
    classes = models.Class.objects.all()
    faculty = models.Faculty.objects.all()
    context = {
        'classes':classes,
        'faculty':faculty,
    }
    return render(request, 'index.html', context)



def addclass(request):
    if request.method == 'POST':
        data = ClassForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/index')
        else:
            data = ClassForm()
    context = {}
    context['form'] = ClassForm()
    return render(request, 'addclass.html', context)



def addstudent(request, id):

    classname = models.Class.objects.get(id=id)
    if request.method=='POST':
        student = request.POST['stud_name']
        idnum = request.POST['idnum']
        email = request.POST['email']
        cgpa = request.POST['cgpa']

        data = models.Student.objects.create(classname=classname, stud_name = student, idnum=idnum, email=email, cgpa=cgpa)
        data.save()
        link = '/class/'+str(id)
        return redirect(link)
    else:
        return render(request, 'addstudent.html')



def addfaculty(request):
    if request.method == 'POST':
        data = FacultyForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/index')
        else:
            data = FacultyForm()
    context = {}
    context['form'] = FacultyForm()
    return render(request, 'addfaculty.html', context)


def viewclass(request, id):
    clas = models.Class.objects.get(id=id)
    students = models.Student.objects.all()
    studcount = models.Student.objects.filter(classname = clas).count()
    
    context = {
        'students':students,
        'class' : clas,
        'count' : studcount,
    }

    return render(request, 'class.html', context)


def updatestudent(request, id):

    student = models.Student.objects.get(id=id)
    context = {
        'student' : student
    }
    if request.method == 'POST':
        student.stud_name = request.POST['stud_name']
        student.idnum = request.POST['idnum']
        student.email = request.POST['email']
        student.cgpa = request.POST['cgpa']
        student.save()
        
        clas = student.classname.classname
        cname = models.Class.objects.values().get(classname = clas)
        link = '/class/'+str(cname['id'])
        
        return redirect(link)
    return render(request, 'updatestudent.html', context)



def deletestudent(request, id):

    student = models.Student.objects.values().get(id=id)
    classid = student['classname_id']

    classi = models.Class.objects.values().get(id = classid)

    std = models.Student.objects.get(id=id)
    std.delete()
    link = '/class/'+str(classi['id'])


    return redirect(link)


def updateclass(request, id):
    clas = models.Class.objects.get(id=id)
    context = {
        'classes':clas
    }
    if request.method == 'POST':
        clas.classname = request.POST['classname']
        clas.save()
        
        return redirect('/index')
    else:
        return render(request, 'updateclass.html', context)


def updatefaculty(request, id):

    data = models.Faculty.objects.get(id=id)
    context = {
        'data':data
    }
    if request.method == 'POST':
        data.facultyName = request.POST['facultyname']
        data.position = request.POST['position']
        data.save()

        return redirect('/index')

    return render(request, 'updatefaculty.html', context)