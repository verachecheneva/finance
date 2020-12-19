from django.urls import path, include
from . views import home, account, register

urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/profile/', account, name='account'),
    path('%5Eregister/', register , name='register'),
    path(r'^register/', register, name='register') #какая-то строка, которая подходит под заданный формат r', r-регулярное выражение
]
