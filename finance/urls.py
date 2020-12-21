"""finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


"""импорт функций, необходимых для реализации перехода между URL-адресами, из библиотек"""
from django.contrib import admin
from django.urls import path, include

"""URL-адрес раздела администрирования"""
"""возвращут домашнюю страничку, делает доступным последующий переход по URL-адресам, указанным в urls.py папки main"""
"""позволяет переходить по URL-адресам внутри /accounts, позволяя использовать систему аутентификации пользователя"""

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
]
