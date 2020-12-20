from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email mustn't be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

class CurrentBudget(models.Model):
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
        
        return (self.moneySum - self.SpendSum)/30
    # def __str__(self):
    #     return self.title

    




