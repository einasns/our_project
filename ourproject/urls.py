from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.products, name='poducts'),
    path('customer/', views.customer,name='customers'),
    path('login/', views.logincustomer,name='login'),
    path('logoutcustomer/', views.logoutcustomer, name='logout'),
    path('logoutadmin/', views.logoutadmin, name='logoutadmin'),
    path('logoutworker/', views.logoutworker, name='logoutworker'),

    path('loginAdmin/', views.loginAdmin,name='loginAdmin'),
    path('homepage/',views.homepage,name='homepage'),
    path('singup/', views.singup,name="sigup"),

]
