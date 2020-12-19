from django.urls import path, include
from . views import home, account, register

urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/profile/', account, name='account'),
    path('register/', register , name='register')
]
