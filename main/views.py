from django.shortcuts import render
from . models import User, CurrentBudget
from django.urls import reverse
from django.views.generic.base import View
from .form import AddBudget

"""объединяем html шаблон с контекстом для домашней страницы"""
def home(request): 
    """получаем все объекты из CurrentBudget и User"""
    budget_is = CurrentBudget.objects.all()
    user_is = User.objects.all()
    return render(request, 'blog/home.html', {'budgets':budget_is, 'Users': user_is})

"""объединяем html шаблон с контекстом для страницы пользователя"""
def account(request):
    """запрашиваем только id пользователя для определения данных на его странице"""
    budget_is = CurrentBudget.objects.filter(user_ID=request.user)
    return render(request, 'blog/account.html', {'budgets':budget_is })

"""импортируем необходимую форму для регистрации"""
from .form import SignUpForm
"""регистрация"""
def register(request):
    """делаем переприсваивание"""
    form_class = SignUpForm 
    """Либо отправляем данные в теле запроса, либо ничего не передаем"""
    user_form = form_class(request.POST or None)
    """если данные отправились в теле запроса"""
    if request.method == 'POST':
        if user_form.is_valid():
            """если форма заполнена корректно, то мы ее присваиваем нововму пользователю и сохраняем нового пользователя"""
            new_user = user_form.save(commit=False)
            """мы не сохраняем парот, а шифруем для созранения безопасности"""
            new_user.set_password(user_form.cleaned_data['password1'])
            """необходимо самостоятельно сохранять потому что commit в значении false"""
            new_user.save()
            """если регистрация прошла успешно, переходим на страницу, где нас уведомляют о регистрации"""
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    """если регистрация не прошла снова попадаем на старницу регистрации"""
    return render(request, 'registration/register.html', {'user_form': user_form})

"""аналогично импортируем необходимую форму для регистрации бюджета"""
def budget_new(request):
    """если мы отправляем данные в теле запроса"""
    if request.method == 'POST':
        """в форму помещаем данные в теле запроса"""
        form = AddBudget(request.POST)
        """если форма заполнена корректно"""
        if form.is_valid():
            """значения бюджета в форме"""
            budget = form.save(commit=False)
            """получаем id пользователя"""
            budget.user_ID = request.user
            """сохраняем бюджет"""
            budget.save()
            """бюджеты определенного пользователя будут доступны по id"""
            budget_is = CurrentBudget.objects.filter(user_ID=request.user)
            """переходим в аккаунт если бюджет успешно доавлен """
            return render(request, 'blog/account.html', {'budgets':budget_is })
        """если что-то не так, то снова попадаем на страницу создания бюджета"""
        return render(request, 'blog/budget_edit.html', {'budgets_form': form })
    form = AddBudget
    return render(request, 'blog/budget_edit.html', {'budget_form': form})

