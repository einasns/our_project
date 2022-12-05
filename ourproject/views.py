from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
	return render(request, 'ourproject/dashboard.html')
def homepage(request):
	return render(request, 'ourproject/homepage.html')


def products(request):
	products=Product.objects.all()
	return render(request, 'ourproject/product.html',{'products':Product})

def customer(request):
	return render(request, 'ourproject/customer.html')