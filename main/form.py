#class AddBudgetForm(forms.Form)
"""производим импорт функций из библиотек, а также моделей и форм из файлов нашего приложения"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CurrentBudget


"""создание формы для регистрации"""
class SignUpForm(UserCreationForm): 
    """заводим переменные, в которые будет помещаться пароль"""
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    
    """создаём класс, для обращения к моделям и их полям"""
    class Meta: 
        model = User  
        """обращаемся к модели User"""
        fields = ('name', 'email', 'password1', 'password2') 
        """обращаемся к полям этой модели"""


class AddBudget(forms.ModelForm): 
    """ создание формы для добавления бюджета
        name - пременная, содержащая название нового бюджета
        moneySum - пременная, содержащая данные о сумме денег пользователя
        SpendToday - пременная, содержащая данные о сумме денег пользователя на текущий день
        SpendSum - пременная, содержащая данные о сумме потраченных денег
        AvaibleSumToday - пременная, содержащая текущую сумму денег"""

    name = forms.CharField(label='Введите название бюджета', widget=forms.TextInput())   
    moneySum = forms.CharField(label='Сколько денег потратили сегодня', widget=forms.NumberInput())
    SpendToday = forms.CharField(label='Ваш бюджет:', widget=forms.NumberInput())
    SpendSum = forms.CharField(label='Всего потрачено', widget=forms.NumberInput())
    AvaibleSumToday = forms.CharField(label='Сегодня Вам доступно', widget=forms.NumberInput())
    
    class Meta:
        """ класс, для обращения и конструирования моделей и их полей
            model - переменная, содержащая конструируемую модель
            fields - переменная, содержащая поля данной модели"""
        model = CurrentBudget 
        fields = ('name', 'moneySum', 'SpendToday', 'SpendSum', 'AvaibleSumToday') 

 