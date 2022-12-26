# from django.test import TestCase,tag
# from django.contrib.auth.models import Group
# from django.urls import reverse
# from django.test import Client
# from ourproject.models import *
# import requests
# from django.contrib.auth.decorators import login_required
# Create your tests here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.test import TestCase,tag
from django.urls import reverse,resolve
from django.test import Client
from ourproject.views import logincustomer,loginAdmin,loginWorker,singup
import unittest
import requests

from ourproject.models import *

#     def setUp(self):
#         self.register_url=reverse('sigup')
#         self.login_url=reverse('login')
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