from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields = ['name', 'bar_code', 'price', 'amount', 'category', 'description']
class ProductFormUPdate(ModelForm):
    class Meta:
        model=Product
        fields = ['name', 'price', 'amount', 'category', 'description']

class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class CreatWorkrForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['user','bank_acccount','name','address','worker_id']
class shiftsForm(ModelForm):
    class Meta:
        model=WeekDayShift
        fields=['worker_name','shift','day']
class FeedbackForm(ModelForm):
    class Meta:
        model=Feedback
        fields=['customer','feedback']