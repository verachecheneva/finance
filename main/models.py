from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

"""информация о том, как переопределить модель авторизации джанго была взята с сайта http://djangonauts.ru/content/pereopredelenie-polej-standartnoj-sistemy-autentif/"""
class UserManager(BaseUserManager):
    """переопределение модели авторизации пользователя, без использования username"""
    """теперь будем использовать менеджеры моделей в миграции"""
    use_in_migrations = True
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email mustn't be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    """определяем еще одну модель авторизации, теперь она необходима для админа c расширенными возможностями"""
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Класс модели пользователя, используя AbstractUser для того, 
    чтобы добавлять доп информацию о пользователе без необходимости создавать доп класс
    username - переменная, содержащая имя пользователя
    email - переменная, содержащая почту пользователя
    USERNAME_FIELD - поле, указывающее имя модели пользователя, используемoe в качестве уникального идентификатора
    REQUIRED_FIELDS - cписок имён полей, которые будут запрашиваться при создании пользователя с помощью команды createsuperuser
    objects - переменная, содержащая новый менеджер модели пользователя"""
    
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    



class CurrentBudget(models.Model):
    """ Создаем модель бюджета
        user_ID - поле, содержащее ID пользователя
        moneySum - поле, содержащее сумму, которой располагает пользователь
        DateOfStart - поле, содержащее дату создания бюджета
        DateOfFinish - поле, содержащее сумму денег потраченную в текущий день
        SpendToday - поле, содержащее потраченную сумму денег
        SpendSum  - поле, содержащее оставшуюся сумму денег
        RestSum  - поле, содержащее доступную пользователю сумму дерег
        AvaibleSumToday  - поле, содержащее доступную пользователю сумму дерег
        name  - поле, содержащее название бюджета"""

    user_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    moneySum = models.IntegerField(default = 0)
    DateOfStart = models.DateTimeField(auto_now_add=True)
    DateOfFinish = models.DateTimeField( null=True, blank=True)
    SpendToday = models.IntegerField(default = 0)
    SpendSum = models.IntegerField(default = 0)
    RestSum = models.IntegerField(default = 0)
    AvaibleSumToday = models.IntegerField(default = 0)
    name = models.CharField(max_length=255)

    def calcSpendSum(self):
        """функция калькулятора потраченной суммы денег , принимающая на вход элемент своего же класса"""
        return (self.moneySum - self.SpendSum)/30


    




