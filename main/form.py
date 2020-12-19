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

    