"""производим импорт необходимых функций из библиотек"""
from django.urls import path, include  
from .views import home, account, register, budget_new

"""описываем URL-адреса, используемые в приложении main"""
"""обработка запроса по URL-адресу главной страницы приложения"""
"""обработка запроса по URL-адресу страницы профиля пользователя"""
"""обработка запроса регулярного выражения (URL-шаблона)"""
"""обработка запроса по URL-адресу страницы создания нового бюджета пользователя"""

urlpatterns = [
    path('home/', home, name='home'),  
    path('accounts/profile/', account, name='account'),  
    path(r'register/', register, name='register'), 
    path('account/new/', budget_new, name='budget_new') 
]
