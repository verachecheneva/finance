"""производим импорт необходимых функций из библиотек"""
from django.urls import path, include  
from .views import home, account, register, budget_new

"""описываем URL-адреса, используемые в приложении main"""
urlpatterns = [
    path('home/', home, name='home'),  """обработка запроса по URL-адресу главной страницы приложения"""
    path('accounts/profile/', account, name='account'),  """обработка запроса по URL-адресу страницы профиля пользователя"""
    path(r'register/', register, name='register'), """обработка запроса регулярного выражения (URL-шаблона)"""
    path('account/new/', budget_new, name='budget_new') """обработка запроса по URL-адресу страницы создания нового бюджета пользователя"""
]
