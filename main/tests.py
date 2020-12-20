from django.test import TestCase
from django.urls import reverse
import requests

class MyTests(TestCase):
    def ViewHomePage(self):
        resp = requests.get('http://127.0.0.1:8000/home/')
        self.assertEqual(resp.status_code, 200)
    def ViewLoginPage(self):
        resp = requests.get('http://127.0.0.1:8000/accounts/login/')
        self.assertEqual(resp.status_code, 200)
    




# Create your tests here.
