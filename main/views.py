from django.shortcuts import render, redirect
from . models import User, CurrentBudget
from django.urls import reverse
from django.views.generic.base import View
from .form import AddBudget


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


def budget_new(request):
    form_budget = AddBudget
    budget_form = form_budget(request.POST or None)
    if request.method == 'POST':
        form = CurrentBudget(request.POST)
        if budget_form.is_valid():
            budget = budget_form.save(commit=True)
            # budget.SpendToday = request.user
            budget.save()
            budget_is = CurrentBudget.objects.filter(user_ID=request.user)
            return render(request, 'blog/account.html', {'budgets':budget_is })
    return render(request, 'blog/budget_edit.html', {'budget_form': budget_form})


    # contacts_form_data = {}

    # if request.method == POST:
    #     # contacts_form_data = request.POST
    #     name = request.POST.get('name')
    #     SpendToday = request.POST.get('SpendToday')

    # contacts_form_data.update({'name':name})

    # context = {
    #     'page_header': 'New Budget',
    #     'contacts_form_data':  contacts_form_data,
    # }
    # return render(request, 'blog/home.html', context)
# class AddBudget(View):
#     def post(self, request, pk):
#         form = AddBudget(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user_ID = pk
#             form.save()
#         return redirect("/")
#         # budget_name = request.POST['name']
#         # budget_SpendToday = request.POST['SpendToday']


# def User_info(request):
#     return render(request, 'main/user_info.html')

# def budget_add(request):
#     if request.method == "GET":
#         budget = AddBudget()
#     return render(request, 'main/budget_add.html', {
#             'form': form
#     })