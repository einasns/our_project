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
from django.urls import reverse
from django.test import Client
import unittest
import requests

from ourproject.models import *
class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('sigup')
        self.login_url=reverse('login')
class LoginTest(BaseTest):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response,'login_customer.html')




# @tag("unit_test")
# class BaseTest(TestCase):
#     @tag('unit-test')
#     def setUp(self):
#         self.singup=reverse('sigup')
#         self.login=reverse('login')
#         self.User={
#             'firstname':'firstname',
#             'lastname':'lastname',
#             'email':'testemail@gmail.com',
#             'username':'username',
#             'password1':'password1',
#             'password2':'password2'
#         }
# @tag("unit_test")
# class loginTest(TestCase):
#     @tag('unit-test')
#     def setUp(self):
#         self.singup = reverse('sigup')
#         self.login = reverse('login')
#         self.User = {
#             'firstname': 'firstname',
#             'lastname': 'lastname',
#             'email': 'testemail@gmail.com',
#             'username': 'username',
#             'password1': 'password1',
#             'password2': 'password2'
#         }
#     @tag('unit-test')
#     def test_login_access_url(self):
#         response = self.client.get('/login/')
#         self.assertEqual(response.status_code, 200)
#
#     @tag('unit-test')
#     def test_login_access_name(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#
#     @tag('unit-test')
#     def test_login_access_url_negative(self):
#         response = self.client.get('/login/')
#         self.assertNotEqual(response.status_code, 300)
#
#     @tag('unit-test')
#     def test_login_access_name_negative(self):
#         response = self.client.get(reverse('login'))
#         self.assertNotEqual(response.status_code, 300)

    # @tag('unit-test')
    # def testLoginUsedTemplate(self):
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
    #
    # @tag('unit-test')
    # def testLogin_NOT_UsedTemplate(self):
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateNotUsed(response, 'homepage.html')
    #
    # @tag('unit-test')
    # def testUserLogin(self):
    #     User.objects.create(username='aa', password='aa')
    #
    #     data = {'username': 'a12', 'password': '1234'}
    #     response = self.client.post(reverse('login'), data=data, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     '''the reason why it redircets to login that's this user doesnt belong to any group'''
    #     self.assertRedirects(response, reverse('login'))
    #
    # @tag('integration-test')
    # def testLoginAndLogout(self):
    #     user.objects.create(username='aa', password='aa')
    #
    #     data = {'username': 'a12', 'password': '1234'}
    #     response = self.client.post(reverse('login'), data=data, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     '''the reason why it redircets to login that's this user doesnt belong to any group'''
    #     self.assertRedirects(response, reverse('login'))
    #     self.assertTemplateUsed(response, 'login_customer.html')
    #     response = self.client.get(reverse('logout'), follow=True)
    #     # Assert
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFalse(response.context["user"].is_authenticated)