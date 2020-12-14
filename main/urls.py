from django.urls import path, include
from . views import home, account

urlpatterns = [
    path('', home, name='home'),
    path('accounts/profile/', account, name='account')
]
