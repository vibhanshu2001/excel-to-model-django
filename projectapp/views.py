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
from .forms import UserForm
from django.views.generic import View
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
@login_required(login_url='handleLogin')
def profilePage(request, id):
    user = User.objects.get(id=id)
    return render(request,'projectapp/profile.html',{'user':user})
@login_required(login_url='handleLogin')
def allprofiles(request):
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request,'projectapp/allprofiles.html',{'user':user})
    else:
        return redirect('index')

@method_decorator(login_required, name='dispatch')
class EditView(View):
  def get(self, request,id):
    user = User.objects.get(id=id)
    fm = UserForm(instance=user)
    return render(request,'projectapp/editprofile.html',{'form':fm,'user':user})
  
  def post(self, request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, request.FILES,instance=user)
    if form.is_valid():
      form.save()
    else:
      print('Reached here')
    return redirect("/")
@method_decorator(login_required, name='dispatch')
class DeleteView(View):
  def post(self, request,id):
    if request.method == 'POST':
        print("Here hu")
        User.objects.filter(id=id).delete()
    else:
        print("Reached here")
    return redirect('/')
    