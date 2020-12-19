from django.shortcuts import render
from . models import User, CurrentBudget
from django.urls import reverse

def home(request):
    budget_is = CurrentBudget.objects.all()
    user_is = User.objects.all()
    return render(request, 'blog/home.html', {'budgets':budget_is, 'Users': user_is})

def account(request):
    budget_is = CurrentBudget.objects.filter(user_ID=request.user)
    return render(request, 'blog/account.html', {'budgets':budget_is })

from .form import SignUpForm

def register(request):
    form_class = SignUpForm
    user_form = form_class(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    return render(request, 'registration/register.html', {'user_form': user_form})





# def User_info(request):
#     return render(request, 'main/user_info.html')

# def budget_add(request):
#     if request.method == "GET":
#         budget = AddBudget()
#     return render(request, 'main/budget_add.html', {
#             'form': form
#     })