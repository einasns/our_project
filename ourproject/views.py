from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



from .models import *
from .forms import CreatUserForm
# Create your views here.
def singup(request):
	if request.user.is_authenticated:
		return redirect('homepage')
	else:
		form = CreatUserForm()
		if request.method == 'POST':
			form = CreatUserForm(request.POST)
			if form.is_valid():
				form.save()
				user=form.cleaned_data.get('username')
				messages.success(request,'Account was created for ' + user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'ourproject/singup.html', context)

def logincustomer(request):

	if request.user.is_authenticated:
		return redirect('homepage')
	else:
		if request.method=='POST':
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('homepage')
			else:
				messages.info(request,'username OR password incorrert')
		context={}
		return render(request, 'ourproject/login_customer.html',context)
def logoutcustomer(request):
	logout(request)
	return redirect('login')
def loginAdmin(request):
	if request.user.is_authenticated:
		return redirect('homepage')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('homepage')
			else:
				messages.info(request, 'username OR password incorrert')
		context = {}
		return render(request, 'ourproject/log_in_admin.html', context)
def loginWorker(request):
	context={}
	return render(request, 'ourproject/log_in_worker.html')
def home(request):
	return render(request, 'ourproject/dashboard.html')

@login_required(login_url='login')
def homepage(request):
	return render(request, 'ourproject/homepage.html')


def products(request):
	products=Product.objects.all()
	return render(request, 'ourproject/product.html',{'products':products})

def customer(request):
	return render(request, 'ourproject/customer.html')

