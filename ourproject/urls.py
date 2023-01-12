from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.products_worker, name='poducts_worker'),
    # path('customer/', views.customers,name='customers'),
    path('workers/', views.workers, name='workers'),

    path('login/', views.logincustomer,name='login'),
    path('logoutcustomer/', views.logoutcustomer, name='logout'),
    path('logoutadmin/', views.logoutadmin, name='logoutadmin'),
    path('logoutworker/', views.logoutworker, name='logoutworker'),
    path('loginAdmin/', views.loginAdmin,name='loginadmin'),
    path('loginWorker/', views.loginWorker,name='loginWorker'),
    path('homepage/',views.homepage,name='homepage'),
    path('homepageadmin/', views.homepage_admin, name='homepage_admin'),
    path('homepagecustomer/', views.homepage_customer, name='homepage_customer'),
    path('homepageworker/', views.homepage_worker, name='homepage_worker'),
    path('Admin_Reviewproduct_list/', views.Admin_Reviewproduct_list, name='Admin_Reviewproduct_list'),
    path('view_customer/',views.customer, name='view_customer'),
    path('delete_worker/<str:pk>/',views.deleteworker, name='delete_worker'),
    path('view_order/',views.view_order, name='view_order'),
    path('customers/',views.customer,name='customer_list'),
    path('add_product_worker/', views.add_product_worker, name='add_product_worker'),
    path('add_product_admin/', views.add_product_admin, name='add_product_admin'),
    path('update_product_worker/<str:pk>/', views.update_product_worker, name='update_product_worker'),
    path('singup/', views.singup,name="sigup"),
    path('search_worker/', views.search_worker, name="search_worker"),
    path('workhours_schedule/', views.workhours_schedule, name="workhours_schedule"),
    path('addtoworkschedule/', views.addtoworkschedule, name="addtoworkschedule"),
    path('delete_product_admin/<str:pk>/', views.delete_product_admin, name="delete_product_admin"),
    path('delete_product_worker/<str:pk>/', views.delete_product_worker, name="delete_product_worker"),
    path('conactus/', views.conactus, name="conactus"),
    path('work_schedule/', views.work_schedule, name="work_schedule"),
    path('search_worker/', views.search_worker,name='search_worker'),

]
