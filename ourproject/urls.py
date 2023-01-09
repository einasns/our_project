from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='poducts'),
    # path('customer/', views.customers,name='customers'),
    path('workers/', views.workers, name='workers'),
    path('login/', views.logincustomer, name='login'),
    path('logoutcustomer/', views.logoutcustomer, name='logout'),
    path('loginAdmin/', views.loginAdmin, name='loginadmin'),
    path('loginWorker/', views.loginWorker, name='loginWorker'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepageadmin/', views.homepage_admin, name='homepage_admin'),
    path('homepageworker/', views.homepage_worker, name='homepage_worker'),
    path('homepagecustomer/', views.homepage_customer, name='homepage_customer'),
    path('customers/', views.customer, name='customer_list'),
    path('singup/', views.singup, name="sigup"),
    path('add/<int:bar_code>/<int:pop>', views.add, name='add'),
    path('delete/<int:bar_cide>/<int:pop>', views.delete, name='delete'),
]
