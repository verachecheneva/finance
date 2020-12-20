from django.test import TestCase, Client
from django.urls import reverse
import requests
from .models import CurrentBudget, User

class TestRegistrationProfile(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username = 'sarah', 
                                            email = 'flower@yandex.ru',
                                            password = 'qazwsx1234')
    
    def test_user_has_profile(self):
        self.client.force_login(self.user, backend=None)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, )




# class MyTests(TestCase):
#     def ViewHomePage(self):
#         resp = requests.get('http://127.0.0.1:8000/home/')
#         self.assertEqual(resp.status_code, 200)
#     def ViewLoginPage(self):
#         resp = requests.get('http://127.0.0.1:8000/accounts/login/')
#         self.assertEqual(resp.status_code, 200)
    




# Create your tests here.
