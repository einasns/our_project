from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func
def unauthenticated_user_login(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Admin':
            return redirect('customers')
        if request.user.is_authenticated:
            return redirect('homepage')

        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allwed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('you are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group == 'Customer':
            return redirect('homepage')
        if group=='Admin':
            return view_func(request, *args, **kwargs)
        if group=='Customer':
            return redirect('homepage')
        else:
            return redirect('home')
        #we need to add the worker in this function
    return wrapper_func

def only_customer(view_func):
    def wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group == 'Admin':
            return redirect('homepage_admin')
        if group=='Customer':
            return view_func(request, *args, **kwargs)
        if group == 'Worker':
            return redirect('homepage_worker')
        else:
            return redirect('home')
        #we need to add the worker in this function
    return wrapper_func
def only_worker(view_func):
    def wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group == 'Admin':
            return redirect('homepage_admin')
        if group=='Worker':
            return view_func(request, *args, **kwargs)
        if group=='Customer':
            return redirect('homepage')

        else:
            return redirect('home')
        #we need to add the worker in this function
    return wrapper_func