from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from itertools import count, repeat, chain
from .forms import CreatUserForm, OrderForm, ProductForm, ProductFormUPdate, shiftsForm
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
                return redirect('homepage')
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


def products_worker(request):
    products = Product.objects.all()

    return render(request, 'ourproject/product_for_worker.html', {'products': products})


def Admin_Reviewproduct_list(request):
    products = Product.objects.all()

    return render(request, 'ourproject/Admin_Reviewproduct_list.html', {'products': products})


def customer(request):
    users_in_group = Group.objects.get(name='Customer').user_set.all()
    # customer =Customer.objects.all()
    cus = {'users_in_group': users_in_group}
    return render(request, 'ourproject/customer_list.html', cus)


def workers(request):
    workers = Worker.objects.all()
    wor = {'workers': Worker}
    return render(request, 'ourproject/workers.html', wor)


def view_customer(request):
    users_in_group = Group.objects.get(name='Customer').user_set.all()
    # customer =Customer.objects.all()
    cus = {'users_in_group': users_in_group}
    return render(request, 'ourproject/customer_list.html', cus)


def deleteworker(request, pk):
    context = {}
    return render(request, 'accounts/delete.html', context)


def view_order(request):
    order = Order.objects.all()
    # customer =Customer.objects.all()
    ord = {'order': order}
    return render(request, 'ourproject/order_list.html', ord)


def work_schedule(request):
    shift_assignments = WeekDayShift.objects.order_by('shift__shift_name', 'day__day_name').values_list(
        'shift__shift_id', 'day__day_id', 'worker_name')
    lis = WeekDay.objects.all().order_by('day_id').values_list('day_name')
    shift_assignment_list = []
    ll = ['shifts/Days:']
    for i in lis:
        ll.append(i)
    shift_assignment_list.append(ll)
    # shift_assignment_list.append(lis)
    shii1 = ['shift1']
    shii2 = ['shift2']
    shii3 = ['shift3']
    shift_assignment_list.append(shii1)
    shift_assignment_list.append(shii2)
    shift_assignment_list.append(shii3)
    for shift in shift_assignments:
        index = [shift[2]]
        if shift[0] == 1:
            shift_assignment_list[1].append(shift[2])
        if shift[0] == 2:
            shift_assignment_list[2].append(shift[2])
        if shift[0] == 3:
            shift_assignment_list[3].append(shift[2])

    context = {'shift_assignment_list': shift_assignment_list}
    return render(request, 'ourproject/buildschedule_forAdmin.html', context)


def addtoworkschedule(request):
    form = shiftsForm()
    if request.method == 'POST':
        day = request.POST.get('day')
        worker = request.POST.get('worker_name')
        shift = request.POST.get('shift')
        instance = WeekDayShift.objects.filter(day=day).filter(worker_name=worker).filter(shift=shift)
        users_in_groub = Group.objects.get(name='Worker').user_set.all()
        ww = users_in_groub.filter(username=worker)
        if ww:
            if not instance:
                form = shiftsForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('work_schedule')
                else:
                    messages.info(request, 'the info is not valid')
            else:
                messages.info(request, 'this shift for some one else already exsited')
        else:
            messages.info(request, 'this is not our worker')

    context = {'form': form}
    return render(request, 'ourproject/add_to_work_schedule.html', context)


def add_product_worker(request):
    form = ProductForm()
    if request.method == 'POST':
        bar_code = request.POST.get('bar_code')
        instance = Product.objects.filter(bar_code=bar_code)
        if not instance:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('poducts_worker')
            else:
                messages.info(request, 'the info is not valid')
        else:
            messages.info(request, 'this product already exsited')
    context = {'form': form}
    return render(request, 'ourproject/add_product_worker.html', context)


def add_product_admin(request):
    form = ProductForm()
    if request.method == 'POST':
        bar_code = request.POST.get('bar_code')
        instance = Product.objects.filter(bar_code=bar_code)
        if not instance:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Admin_Reviewproduct_list')
            else:
                messages.info(request, 'the info is not valid')
        else:
            messages.info(request, 'this product already exsited')
    context = {'form': form}
    return render(request, 'ourproject/add_product_admin.html', context)


def update_product_worker(request, pk):
    product = Product.objects.get(bar_code=pk)
    form = ProductFormUPdate(instance=product)
    if request.method == 'POST':
        form = ProductFormUPdate(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('poducts_worker')
    context = {'form': form}
    return render(request, 'ourproject/update_product_worker.html', context)


def delete_product_admin(request, pk):
    product = Product.objects.get(bar_code=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Admin_Reviewproduct_list')
    context = {'item': product}
    return render(request, 'ourproject/delete_product_admin.html', context)


def delete_product_worker(request, pk):
    product = Product.objects.get(bar_code=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('poducts_worker')
    context = {'item': product}
    return render(request, 'ourproject/delete_product_worker.html', context)
