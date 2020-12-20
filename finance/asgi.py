"""
ASGI config for finance project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# ASGI — это интерфейс для коммуникации между приложениями и серверами.
# Позволяет асинхронным Python серверам и приложениям взаимодействовать друг с другом.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings')

application = get_asgi_application()
