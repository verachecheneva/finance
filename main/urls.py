from django.urls import path, include
from .views import home, account, register, budget_new


urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/profile/', account, name='account'),
    path(r'register/', register, name='register'), #какая-то строка, которая подходит под заданный формат r', r-регулярное выражение
    path('account/new/', budget_new, name='budget_new')
]
