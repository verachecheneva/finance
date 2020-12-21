from django.test import Client, TestCase
from django.urls import reverse
import requests
from .models import CurrentBudget, User

class TestRegistrationProfile(TestCase):
    """регистрируем пользователя, с которым будут проходить тесты"""
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(name = 'sarah', email='flower@gmail.com', password='qazwsx1234')

    """Проверяем что этот пользователь имеет профиль"""
    def test_user_has_profile(self):
        self.client.force_login(self.user, backend=None)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
    

    """тест, нацеленный на проверку корректности добавленного бюджета"""
    def test_test_registered_user_new_budget(self):
        """инструмент тестирования, эмулирующий авторизацию пользователя на нашем сайте"""
        self.client.force_login(self.user, backend=None) 
        """возвращение объекта Response в ответ на отправку тестовым клиентом запроса"""
        self.client.post(reverse('budget_new'),{'name': 'Test', 'SpendToday': 222, 'moneySum': 100, 'AvaibleSumToday' : 4, 'SpendSum': 4}) 
        """проверка равенства, если условие не выполняется, следует провал теста"""
        self.assertEqual(CurrentBudget.objects.count(), 1) 
        budget = CurrentBudget.objects.first()

        """проверка равенста заданного тестом значения и ожидаемого результата"""
        self.assertEqual(budget.name, 'Test') 
        self.assertEqual(budget.user_ID, self.user)
        self.assertEqual(budget.SpendToday, 222)
