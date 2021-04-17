from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ['username','first_name', 'last_name', 'email']
  labels = {'username':'User Name','first_name':'First Name', 'email': 'Email ID', 'last_name':'Last Name'}
  widgets = {
   'username':forms.TextInput(attrs={'class':'form-control'}),
   'first_name':forms.TextInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
   'last_name':forms.TextInput(attrs={'class':'form-control'}),
  }




      