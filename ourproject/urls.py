from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.products_worker, name='poducts_worker'),
    # path('customer/', views.customers,name='customers'),
    path('workers/', views.workers, name='workers'),

    path('login/', views.logincustomer,name='login'),
    path('logoutcustomer/', views.logoutcustomer, name='logout'),

    path('loginAdmin/', views.loginAdmin,name='loginadmin'),
    path('loginWorker/', views.loginWorker,name='loginWorker'),
    path('homepage/',views.homepage,name='homepage'),
    path('homepageadmin/', views.homepage_admin, name='homepage_admin'),
    path('homepageworker/', views.homepage_worker, name='homepage_worker'),
    path('Admin_Reviewproduct_list/', views.Admin_Reviewproduct_list, name='Admin_Reviewproduct_list'),
    path('view_customer/',views.customer, name='view_customer'),
    path('delete_worker/<str:pk>/',views.deleteworker, name='delete_worker'),
    path('view_order/',views.view_order, name='view_order'),

    path('customers/',views.customer,name='customer_list'),
    path('add_product_worker/', views.add_product_worker, name='add_product_worker'),
    path('update_product_worker/<str:pk>/', views.update_product_worker, name='update_product_worker'),

    path('singup/', views.singup,name="sigup"),
    path('work_schedule/', views.work_schedule, name="work_schedule"),
    path('addtoworkschedule/', views.addtoworkschedule, name="addtoworkschedule"),

]
