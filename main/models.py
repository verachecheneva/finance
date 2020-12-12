from django.db import models
#ПРИВЕТИКИ
class CurrentBudget(models.Model):
    user_ID = models.CharField(max_length=255)
    budget_ID = models.CharField(max_length=255)
    moneySum = models.IntegerField(default = 0)
    DateOfStart = models.DateTimeField( null=True, blank=True)
    DateOfFinish = models.DateTimeField( null=True, blank=True)
    SpendToday = models.IntegerField(default = 0)
    SpendSum = models.IntegerField(default = 0)
    RestSum = models.IntegerField(default = 0)
    AvaibleSumToday = models.IntegerField(default = 0)

class Data(models.Model):
    user_ID = models.CharField(max_length=255)
    SpendSum = models.IntegerField(default = 0)
    data = models.DateTimeField( null=True, blank=True)

class User(models.Model):
    user_ID = models.CharField(max_length=255)
    budget_ID = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
