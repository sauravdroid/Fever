from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request,'Studemt/index.html')


def register(request):
    if request.method == 'GET':
        form = StudentRegisterForm()
        subjects = Subject.objects.all()
        return render(request, 'Studemt/register.html',
                      {'form': form, 'preference_form': ApplicationForm(), 'subjects': subjects})
    else:
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        application_form = ApplicationForm(request.POST)
        user = User(username=username, first_name=firstname, last_name=lastname)
        user.set_password(password)
        user.save()
        form = StudentRegisterForm(request.POST)
        if form.is_valid() and application_form.is_valid():
            student = form.save(commit=False)
            application_f = application_form.save(commit=False)
            application_f.serial = 0
            application_f.student = user
            application_f.date_time = timezone.now()
            student.student = user
            student.save()
            application_f.save()
        return HttpResponse("Successfully Registered")


@login_required(login_url='student:login')
def application(request):
    if request.method == 'GET':
        form = ApplicationForm()
        return render(request, 'Studemt/applications.html', {'form': form})
    else:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.serial = 0
            user.student = request.user
            user.date_time = timezone.now()
            user.save()
            return HttpResponse('Successfully Registered')


def user_login(request):
    if request.user.is_authenticated():
        return redirect('student:application')
    else:
        if request.method == 'GET':
            return render(request, 'Studemt/login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student:application')
            else:
                return render(request, 'Studemt/login.html', {'error_message': 'Wrong Username or Password'})


@login_required(login_url='student:login')
def user_logout(request):
    logout(request)
    return redirect('student:login')


def student_list(request):
    if request.method == 'GET':
        students = Student.objects.order_by('rank')
        hello_set = Hello.objects.all()
        return render(request, 'Studemt/student_list.html', {'students': students, 'hello_set': hello_set})


def demo(request):
    subjects = Subject.objects.all()
    return render(request, 'Studemt/app_js.html', {'subjects': subjects})
