from django.shortcuts import render
from . models import User, CurrentBudget
from django.urls import reverse

def home(request):
    budget_is = CurrentBudget.objects.all()
    user_is = User.objects.all()
    return render(request, 'blog/home.html', {'budgets':budget_is, 'Users': user_is})

def account(request):
    budget_is = CurrentBudget.objects.all()
    user_is = User.objects.all()
    return render(request, 'blog/account.html', {'budgets':budget_is, 'Users': user_is})




# def User_info(request):
#     return render(request, 'main/user_info.html')

# def budget_add(request):
#     if request.method == "GET":
#         budget = AddBudget()
#     return render(request, 'main/budget_add.html', {
#             'form': form
#     })