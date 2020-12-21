from django.shortcuts import render
from . models import User, CurrentBudget
from django.urls import reverse
from django.views.generic.base import View
from .form import AddBudget


def home(request): 
    """объединяем html шаблон с контекстом для домашней страницы"""
    """получаем все объекты из CurrentBudget и User"""
    budget_is = CurrentBudget.objects.all()
    user_is = User.objects.all()
    return render(request, 'blog/home.html', {'budgets':budget_is, 'Users': user_is})


def account(request):
    """объединяем html шаблон с контекстом для страницы пользователя"""
    """запрашиваем только id пользователя для определения данных на его странице"""
    budget_is = CurrentBudget.objects.filter(user_ID=request.user)
    return render(request, 'blog/account.html', {'budgets':budget_is })


from .form import SignUpForm

def register(request):
    """страница регистрации, если регистрация проходит успешно пользователь переходит на следующую страницу, иначе остается на странице регистрации"""
    form_class = SignUpForm 
    user_form = form_class(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    return render(request, 'registration/register.html', {'user_form': user_form})

"""аналогично импортируем необходимую форму для регистрации бюджета"""
def budget_new(request):
    """регистрируем новый бюджет, если форма отправлена успешна переходим на страницу аккаунта, иначе остаемся на странице добавления бюджета"""
    if request.method == 'POST':
        form = AddBudget(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user_ID = request.user
            budget.save()
            budget_is = CurrentBudget.objects.filter(user_ID=request.user)
            return render(request, 'blog/account.html', {'budgets':budget_is })
        return render(request, 'blog/budget_edit.html', {'budgets_form': form })
    form = AddBudget
    return render(request, 'blog/budget_edit.html', {'budget_form': form})

