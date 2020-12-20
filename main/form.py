#class AddBudgetForm(forms.Form)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CurrentBudget

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')

# создание бюджета
class AddBudget(forms.ModelForm):
    name = forms.CharField(label='Введите название бюджетаб', widget=forms.TextInput())
    SpendToday = forms.CharField(label='Сколько денег потратили сеглня', widget=forms.NumberInput())
    class Meta:
        model = CurrentBudget
        fields = ('name', 'SpendToday')

    # def save(self):
    #     new_budget = CurrentBudget.objects.create(
    #         name=self.cleaned_data['name'],
    #         SpendToday=self.cleaned_data['SpendToday']
    #     )
    #     return new_budget