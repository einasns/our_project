from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import CreatUserForm
from .decorators import unauthenticated_user,allwed_users,admin_only,unauthenticated_user_login
# Create your views here.
@unauthenticated_user
def singup(request):
	form = CreatUserForm()
	if request.method == 'POST':
		form = CreatUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			group=Group.objects.get(name='Customer')
			user.groups.add(group)
			messages.success(request,'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}
	return render(request, 'ourproject/singup.html', context)
@unauthenticated_user
def logincustomer(request):
	users_in_group = Group.objects.get(name='Customer').user_set.all()
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			if user in users_in_group:
				login(request,user)
				return redirect('homepage')
			else:
				messages.info(request, 'username OR password incorrert')
		else:
			messages.info(request,'username OR password incorrert')
	context={}
	return render(request, 'ourproject/login_customer.html',context)
def logoutcustomer(request):
	logout(request)
	return redirect('login')
def loginAdmin(request):
	context={}
	return render(request, 'ourproject/log_in_admin.html')
def home(request):
	return render(request, 'ourproject/dashboard.html')

@login_required(login_url='login')
@admin_only
def homepage(request):
	return render(request, 'ourproject/homepage.html')


def products(request):

	products=Product.objects.all()

	return render(request, 'ourproject/product.html',{'products':products})

def customer(request):
	return render(request, 'ourproject/customer.html')

