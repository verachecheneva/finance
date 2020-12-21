from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

"""переопределение модели авторизации пользователя"""
"""username не используется"""
class UserManager(BaseUserManager):
    """теперь будем использовать менеджеры моделей в миграции"""
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """избавляемся от username, вместо него обязательным полем будет email"""
        if not email:
            raise ValueError("The given email mustn't be set")
        """приводим email к нужному виду, все буквы должны быть в нижнем регистре"""
        """Создаем пользователя"""
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        """используем using параметр для определения используемой базы данных, это дефолтное знаение, оно прописасно в settings.py"""
        user.save(using=self._db)
        return user
    """определяем еще одну модель авторизации, теперь она необходима для админа"""
    def create_superuser(self, email, password, **extra_fields):
        """определяем возможности такого пользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        """Пользователь обязательно должен иметь указанные выше поля"""
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

"""Создаём класс модели пользователя, используя AbstractUser для того, чтобы добавлять доп информацию о пользователе без необходимости создавать доп класс"""
class User(AbstractUser):
    """присваивание, ответственное за наличие имени пользователя"""
    username = None
    """поле, отвечающее за почту пользователя"""
    email = models.EmailField(_('email address'), unique=True)
    """поле, отвечающее за имя пользователя"""
    name = models.CharField(max_length=255)
    """строка, указывающая имя поля модели пользователя, используемая в качестве уникального идентификатора"""
    USERNAME_FIELD = 'email'
    """Список имён полей, которые будут запрашиваться при создании пользователя с помощью команды createsuperuser"""
    REQUIRED_FIELDS = []
    """Назначаем новый менеджер модели пользователя"""
    objects = UserManager()
    


"""Создаем класс модели бюджета"""
class CurrentBudget(models.Model):
    """Указываем поле, отвечающее за ID пользователя"""
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    """Указываем поле, отвечающее за сумму, которой располагает пользователь"""
    moneySum = models.IntegerField(default = 0)
    """Указываем поле, отвечающее за дату создания бюджета"""
    DateOfStart = models.DateTimeField(auto_now_add=True)
    """Указываем поле, отвечающее за дату окончания действия бюджета"""
    DateOfFinish = models.DateTimeField( null=True, blank=True)
    """Указываем поле, отвечающее за сумму денег потраченную в текущий день"""
    SpendToday = models.IntegerField(default = 0)
    """Указываем поле, отвечающее за потраченную сумму денег"""
    SpendSum = models.IntegerField(default = 0)
    """Указываем поле, отвечающее за оставшуюся сумму денег"""
    RestSum = models.IntegerField(default = 0)
    """Указываем поле, отвечающее за доступную пользователю сумму дерег"""
    AvaibleSumToday = models.IntegerField(default = 0)
    """Указываем поле, отвечающее за название бюджета"""
    name = models.CharField(max_length=255)

    """функция калькулятора потраченной суммы денег"""
    def calcSpendSum(self):
        
        return (self.moneySum - self.SpendSum)/30


    




