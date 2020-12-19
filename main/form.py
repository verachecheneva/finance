#class AddBudgetForm(forms.Form)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CurrentBudget

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2',)
    