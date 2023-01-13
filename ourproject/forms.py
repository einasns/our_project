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


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


class WorkerForm(ModelForm):
    class Meta:
        model= Worker
        fields='__all__'
        exclude=['user']
class orderform(ModelForm):
    class Meta:
        model= Order
        fields='__all__'
class Createuserform(UserCreationForm):
    class Meta:
        model =Worker
        fields=['name','phone','address','worker_id','bank_acccount']



