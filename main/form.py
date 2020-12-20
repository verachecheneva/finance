#class AddBudgetForm(forms.Form)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CurrentBudget

class SignUpForm(UserCreationForm):  #создаём форму для регистрации
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput) #заводим переменные, в которые будет помещаться пароль
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    class Meta: #создаём класс, для обращения к моделям и их полям
        model = User  #обращаемся к модели User
        fields = ('name', 'email', 'password1', 'password2') #обращаемся к полям этой модели

# создание бюджета
class AddBudget(forms.ModelForm): #создаём форму для регистрации
    name = forms.CharField(label='Введите название бюджетаб', widget=forms.TextInput())   #заводим переменные, в которых будет храниться информация о бюджете
    moneySum = forms.CharField(label='Сколько денег потратили сеглня', widget=forms.NumberInput())
    SpendToday = forms.CharField(label='Ваш бюджет:', widget=forms.NumberInput())
    SpendSum = forms.CharField(label='Всего потрачено', widget=forms.NumberInput())
    AvaibleSumToday = forms.CharField(label='Сегодня Вам доступно', widget=forms.NumberInput())
    class Meta: #создаём класс, для обращения к моделям и их полям
        model = CurrentBudget #обращаемся к модели CurrentBudget
        fields = ('name', 'moneySum', 'SpendToday', 'SpendSum', 'AvaibleSumToday') #обращаемся к полям этой модели

 