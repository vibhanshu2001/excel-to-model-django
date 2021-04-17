from django.shortcuts import render,redirect
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
def indexPage(request):
    return render(request,'projectapp/index.html')
@login_required(login_url='handleLogin')
def simple_upload(request):
    if request.method =='POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        if not new_person.name.endswith('xlsx'):
            messages.error(request,'Please upload only .xlsx file')
            return render(request,'projectapp/upload.html')
        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            value=Person(
                data[0],data[1],data[2],data[3]
            )
            value.save()
        messages.success(request,'Successfull')
    return render(request,'projectapp/upload.html')
@login_required(login_url='handleLogin')
def alldata(request):
    data = Person.objects.all()
    # print(data[0].name)
    return render(request,'projectapp/alldata.html',{'data':data})

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('handleLogin')

    return render(request, 'projectapp/login.html')
def handleLogout(request):
    logout(request)
    messages.info(request,'Successfully logged out')
    return redirect('handleLogin')
    