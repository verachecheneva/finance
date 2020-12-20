from django.test import Client, TestCase
from django.urls import reverse
import requests
from .models import CurrentBudget, User

class TestRegistrationProfile(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects._create_user(name = 'sarah', email='flower@gmail.com', password='qazwsx1234')

    def test_user_has_profile(self):
        self.client.force_login(self.user, backend=None)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
    
    def test_test_registered_user_new_budget(self):
        self.client.force_login(self.user, backend=None)
        self.client.post(reverse('budget_new'),{'name': 'Test', 'SpendToday': 222, 'moneySum': 100, 'AvaibleSumToday' : 4, 'SpendSum': 4})
        self.assertEqual(CurrentBudget.objects.count(), 1)
        budget = CurrentBudget.objects.first()
        self.assertEqual(budget.name, 'Test')
        self.assertEqual(budget.user_ID, self.user)
        self.assertEqual(budget.SpendToday, 222)
