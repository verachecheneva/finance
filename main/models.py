from django.db import models

# обновила
# обновляю
# прив
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # user_ID = models.CharField(max_length=255) автоматом
    # budget_ID = models.CharField(max_length=255) обратные ссылки

class CurrentBudget(models.Model):
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    moneySum = models.IntegerField(default = 0)
    DateOfStart = models.DateTimeField( null=True, blank=True)
    DateOfFinish = models.DateTimeField( null=True, blank=True)
    SpendToday = models.IntegerField(default = 0)
    SpendSum = models.IntegerField(default = 0)
    RestSum = models.IntegerField(default = 0)
    AvaibleSumToday = models.IntegerField(default = 0)




