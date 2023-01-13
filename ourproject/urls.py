from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.products_worker, name='poducts_worker'),
    # path('customer/', views.customers,name='customers'),
    path('workers/', views.workers, name='workers'),
    path('addworker/', views.add_worker, name='add_worker'),
    path('addworker2/', views.add_worker2, name='add_worker2'),

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
    path('add_product_admin/', views.add_product_admin, name='add_product_admin'),
    path('update_product_worker/<str:pk>/', views.update_product_worker, name='update_product_worker'),

    path('singup/', views.singup,name="sigup"),
    path('work_schedule/', views.work_schedule, name="work_schedule"),
    path('addtoworkschedule/', views.addtoworkschedule, name="addtoworkschedule"),
    path('delete_product_admin/<str:pk>/', views.delete_product_admin, name="delete_product_admin"),
    path('delete_product_worker/<str:pk>/', views.delete_product_worker, name="delete_product_worker"),
    path('conactus/', views.conactus, name="conactus"),
    path('best_sales/',views.best_sales, name="best_sales"),

    path('review_my_order/<str:pk>/', views.review_my_order, name="review_my_order"),
    path('deleteworkschedule/', views.deleteworkschedule, name="deleteworkschedule"),

    path('review_my_order/<str:pk>/', views.review_my_order, name="review_my_order"),
    path('worker_view_feedback/', views.worker_view_feedback, name="worker_view_feedback"),
    path('delete_product_admin/<str:pk>/', views.delete_product_admin, name="delete_product_admin"),
    path('delete_product_worker/<str:pk>', views.delete_product_worker, name="delete_product_worker"),
    path('add_to_cart/<str:bar_code>/<str:username>/', views.add_to_cart, name="add_to_cart"),
    path('my_cart/', views.my_cart, name="my_cart"),
    path('reviewfeedbackcustomer/', views.reviewfeedback, name="reviewfeedbackcustomer"),
    path('editprofile', views.editprofile,name="editprofile"),
    path('admindeleteworker/<str:pk>/', views.admindeleteworker, name="admin_delete_worker"),
    path('create_order/',views.createorder,name="create_order")

]
