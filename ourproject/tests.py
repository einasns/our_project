from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.test import TestCase,tag
from django.urls import reverse,resolve
from django.test import Client
from ourproject.views import logincustomer,loginAdmin,loginWorker,singup,products_worker,add_product_worker,update_product_worker,review_my_order,work_schedule,best_sales
import unittest
import requests
import json
from django.shortcuts import render,get_object_or_404,redirect
from ourproject.models import *

class Login_customerTest(TestCase):
    def testCustomerLoginUsedTemplate(self):
        response =self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/login_customer.html')
    def testCustomerLoginNotUsedTemplate(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/singup.html')
    def testLoginAccessUrl(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    def testloginaccessUrlNegetve(self):
        response = self.client.get('/login/')
        self.assertNotEqual(response.status_code, 300)
    def testloginUrlIsResolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,logincustomer)
    def testloginAccessName(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    def testLoginAccessNameNegative(self):
        response = self.client.get(reverse('login'))
        self.assertNotEqual(response.status_code, 300)
class Login_adminTest(TestCase):
    def testAdminLoginUsedTemplate(self):
        response =self.client.get(reverse('loginadmin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/log_in_admin.html')
    def testAdminLoginNotUsedTemplate(self):
        response = self.client.get(reverse('loginadmin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/singup.html')
    def testLoginAccessUrl(self):
        response = self.client.get('/loginAdmin/')
        self.assertEqual(response.status_code, 200)
    def testloginaccessUrlNegetve(self):
        response = self.client.get('/loginAdmin/')
        self.assertNotEqual(response.status_code, 300)
    def testloginUrlIsResolved(self):
        url = reverse('loginadmin')
        self.assertEquals(resolve(url).func,loginAdmin)
    def testloginAccessName(self):
        response = self.client.get(reverse('loginadmin'))
        self.assertEqual(response.status_code, 200)
    def testLoginAccessNameNegative(self):
        response = self.client.get(reverse('loginadmin'))
        self.assertNotEqual(response.status_code, 300)
class Login_WorkerTest(TestCase):
    def testWorkerLoginUsedTemplate(self):
        response =self.client.get(reverse('loginWorker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/log_in_worker.html')
    def testWorkerLoginNotUsedTemplate(self):
        response = self.client.get(reverse('loginWorker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/singup.html')
    def testLoginAccessUrl(self):
        response = self.client.get('/loginWorker/')
        self.assertEqual(response.status_code, 200)
    def testloginaccessUrlNegetve(self):
        response = self.client.get('/loginWorker/')
        self.assertNotEqual(response.status_code, 300)
    def testloginUrlIsResolved(self):
        url = reverse('loginWorker')
        self.assertEquals(resolve(url).func,loginWorker)
    def testloginAccessName(self):
        response = self.client.get(reverse('loginWorker'))
        self.assertEqual(response.status_code, 200)
    def testLoginAccessNameNegative(self):
        response = self.client.get(reverse('loginWorker'))
        self.assertNotEqual(response.status_code, 300)
class singupTest(TestCase):
    def testsingupUsedTemplate(self):
        response =self.client.get(reverse('sigup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/singup.html')
    def testsingupNotUsedTemplate(self):
        response = self.client.get(reverse('sigup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/dashboard.html')
    def testsingupAccessUrl(self):
        response = self.client.get('/singup/')
        self.assertEqual(response.status_code, 200)
    def testsingupaccessUrlNegetve(self):
        response = self.client.get('/singup/')
        self.assertNotEqual(response.status_code, 300)
    def testsingupUrlIsResolved(self):
        url = reverse('sigup')
        self.assertEquals(resolve(url).func,singup)
    def testsingupAccessName(self):
        response = self.client.get(reverse('sigup'))
        self.assertEqual(response.status_code, 200)
    def testsingupAccessNameNegative(self):
        response = self.client.get(reverse('sigup'))
        self.assertNotEqual(response.status_code, 300)
class review_worker_productTest(TestCase):
    def testreview_worker_productUsedTemplate(self):
        response =self.client.get(reverse('poducts_worker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/product_for_worker.html')
    def testreview_worker_productNotUsedTemplate(self):
        response = self.client.get(reverse('poducts_worker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/dashboard.html')
    def testreview_worker_productAccessUrl(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
    def testreview_worker_productpaccessUrlNegetve(self):
        response = self.client.get('/products/')
        self.assertNotEqual(response.status_code, 300)
    def testreview_worker_productUrlIsResolved(self):
        url = reverse('poducts_worker')
        self.assertEquals(resolve(url).func,products_worker)
    def testreview_worker_productAccessName(self):
        response = self.client.get(reverse('poducts_worker'))
        self.assertEqual(response.status_code, 200)
    def testreview_worker_productAccessNameNegative(self):
        response = self.client.get(reverse('poducts_worker'))
        self.assertNotEqual(response.status_code, 300)
class add_product_workerTest(TestCase):
    def testadd_product_workerUsedTemplate(self):
        response =self.client.get(reverse('add_product_worker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/add_product_worker.html')
    def testadd_product_workerNotUsedTemplate(self):
        response = self.client.get(reverse('add_product_worker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/dashboard.html')
    def testadd_product_workerAccessUrl(self):
        response = self.client.get('/add_product_worker/')
        self.assertEqual(response.status_code, 200)
    def testadd_product_workerpaccessUrlNegetve(self):
        response = self.client.get('/add_product_worker/')
        self.assertNotEqual(response.status_code, 300)
    def testadd_product_workerUrlIsResolved(self):
        url = reverse('add_product_worker')
        self.assertEquals(resolve(url).func,add_product_worker)
    def testadd_product_workerAccessName(self):
        response = self.client.get(reverse('add_product_worker'))
        self.assertEqual(response.status_code, 200)
    def testadd_product_workerAccessNameNegative(self):
        response = self.client.get(reverse('add_product_worker'))
        self.assertNotEqual(response.status_code, 300)
##########################################################################################################
class update_product_workerTest(TestCase):
    def testupdate_product_workerUsedTemplate(self):
        response =self.client.get(reverse('update_product_worker'),{'bar_code': '45'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/update_product_worker.html')
    def testupdate_product_workerNotUsedTemplate(self):
        response = self.client.get(reverse('update_product_worker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/dashboard.html')
    def testupdate_product_workerrAccessUrl(self):
        response = self.client.get('/update_product_worker/',{'bar_code': '45'})
        self.assertEqual(response.status_code, 200)
    def testupdate_product_workerpaccessUrlNegetve(self):
        response = self.client.get('/update_product_worker/',{'bar_code': '44'})
        self.assertNotEqual(response.status_code, 300)
    def testupdate_product_workerUrlIsResolved(self):
        url = reverse('update_product_worker',{'bar_code': 45})
        self.assertEquals(resolve(url).func,update_product_worker,{'bar_code': 45})
    def testupdate_product_workerAccessName(self):
        response = self.client.get(reverse('update_product_worker',{'bar_code': 45}))
        self.assertEqual(response.status_code, 200)
    def testupdate_product_workerAccessNameNegative(self):
        response = self.client.get(reverse('update_product_worker',{'bar_code': 45}))
        self.assertNotEqual(response.status_code, 300)
# class customer_review_hisorderTest(TestCase):
#     def testcustomer_review_hisorderUsedTemplate(self):
#         response =self.client.get(reverse('review_my_order'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateNotUsed(response,'ourproject/review_myorder_customer.html')
#     def testcustomer_review_hisorderNotUsedTemplate(self):
#         response = self.client.get(reverse('review_my_order'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateNotUsed(response, 'ourproject/dashboard.html')
#     def testcustomer_review_hisorderAccessUrl(self):
#         response = self.client.get('/review_my_order/')
#         self.assertEqual(response.status_code, 404)
#     def testcustomer_review_hisorderpaccessUrlNegetve(self):
#         response = self.client.get('/review_my_order/')
#         self.assertNotEqual(response.status_code, 300)
#     def testcustomer_review_hisorderUrlIsResolved(self):
#         url = reverse('review_my_order')
#         self.assertEquals(resolve(url).func,add_product_worker)
#     def testcustomer_review_hisorderAccessName(self):
#         response = self.client.get(reverse('review_my_order'))
#         self.assertEqual(response.status_code, 200)
#     def testacustomer_review_hisorderAccessNameNegative(self):
#         response = self.client.get(reverse('review_my_order'))
#         self.assertNotEqual(response.status_code, 300)
# class work_scheduleTest(TestCase):
    def testwork_scheduleUsedTemplate(self):
        response =self.client.get(reverse('work_schedule'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'ourproject/buildschedule_forAdmin.html')
    def testcwork_scheduleNotUsedTemplate(self):
        response = self.client.get(reverse('work_schedule'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'ourproject/dashboard.html')
    def testwork_scheduleAccessUrl(self):
        response = self.client.get('/work_schedule/')
        self.assertEqual(response.status_code, 200)
    def testwork_schedulepaccessUrlNegetve(self):
        response = self.client.get('/work_schedule/')
        self.assertNotEqual(response.status_code, 300)
    def testwork_scheduleUrlIsResolved(self):
        url = reverse('work_schedule')
        self.assertEquals(resolve(url).func,work_schedule)
    def testwork_scheduleAccessName(self):
        response = self.client.get(reverse('work_schedule'))
        self.assertEqual(response.status_code, 200)
    def testwork_scheduleAccessNameNegative(self):
        response = self.client.get(reverse('work_schedule'))
        self.assertNotEqual(response.status_code, 300)
class best_salesTest(TestCase):
    def testbest_salesUrlIsResolved(self):
        url = reverse('best_sales')
        self.assertEquals(resolve(url).func,best_sales)
