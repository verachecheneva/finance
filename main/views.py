from django.shortcuts import render
from .models import User


def index(request):
    tasks = User.objects.all()
    return render(request, 'main/index.html',)


def about(request):
    return render(request, 'main/about.html')

# Create your views here.
