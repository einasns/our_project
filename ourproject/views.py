from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import CreatUserForm
from .decorators import unauthenticated_user, allwed_users, admin_only, only_worker, only_customer


# Create your views here.
@unauthenticated_user
def singup(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'ourproject/singup.html', context)


def logincustomer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Customer').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('homepage_customer')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'ourproject/login_customer.html', context)


def logoutcustomer(request):
    logout(request)
    return redirect('login')


# this functions do the work of the log in
@unauthenticated_user
def loginAdmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_groub = Group.objects.get(name='Admin').user_set.all()
            if user in users_in_groub:
                login(request, user)
                return redirect('homepage_admin')
            else:
                messages.info(request, 'Username OR Password incorrert')
        else:
            messages.info(request, 'username OR Password incorrert')
    context = {}
    return render(request, 'ourproject/log_in_admin.html', context)


def loginWorker(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_groub = Group.objects.get(name='Worker').user_set.all()
            if user in users_in_groub:
                login(request, user)
                return redirect('homepage_worker')
            else:
                messages.info(request, 'Username OR Password incorrert')
        else:
            messages.info(request, 'username OR Password incorrert')
    context = {}
    return render(request, 'ourproject/log_in_worker.html', context)


def home(request):
    return render(request, 'ourproject/dashboard.html')


@login_required(login_url='loginAdmin')
@only_customer
def homepage(request):
    return render(request, 'ourproject/homepage.html')


@login_required(login_url='login')
@admin_only
def homepage_admin(request):
    return render(request, 'ourproject/homepage_admin.html')


@login_required(login_url='login')
@only_worker
def homepage_worker(request):
    return render(request, 'ourproject/homepage_worker.html')


def homepage_customer(request):
    return render(request, 'ourproject/homepage_customer.html')


def products(request):
    products = Product.objects.all()

    return render(request, 'ourproject/product.html', {'products': products})


def customer(request):
    users_in_group = Group.objects.get(name='Customer').user_set.all()
    # customer =Customer.objects.all()
    cus = {'users_in_group': users_in_group}
    return render(request, 'ourproject/customer_list.html', cus)


def workers(request):
    workers = Worker.objects.all()
    wor = {'workers': Worker}
    return render(request, 'ourproject/workers.html', wor)


'''
def delete_product(request, bar_code):
    product = Product.objects.get(pr=bar_code)
    product.delete()
	return redirect('customer')

def add_product(request):
	submitted=False
	if request.method
'''


def add(request, bar_code, pop):
    originalObj = products.objects.get(id=bar_code)
    if originalObj.amount == 0:
        productsForCustomer = products.objects.all();
        return render(request, "homepage_customer.html", {'productsForCustomer': productsForCustomer})
    else:
        originalObj.amount = pop + 1
        originalObj.save()
        productsForCustomer = products.objects.all();
        return render(request, "homepage_customer.html", {'productsForCustomer': productsForCustomer})


def delete(request, bar_code, pop):
    originalObj = products.objects.get(id=bar_code)
    if originalObj.amount == 0:
        productsForCustomer = products.objects.all();
        return render(request, "homepage_customer.html", {'productsForCustomer': productsForCustomer})
    originalObj.amount = pop - 1
    originalObj.save()
    productsForCustomer = products.objects.all();
    return render(request, "homepage_customer.html", {'productsForCustomer': productsForCustomer})
