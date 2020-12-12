from django.db import models

class User(models.Model):
    user_ID = models.CharField(max_length=100)
    budget_ID = models.CharField(max_length=50)
    email = models.EmailField()
    #password = models.CharField()
    name = models.CharField(max_length=255)


class CurrentBudget(models.Model):
    user_ID = models.ManyToManyField (User)
    budget_ID = models.ManyToManyField (User)
    moneySum = models.IntegerField(default = 0)
    DateOfStart = models.DateTimeField( null=True, blank=True)
    DateOfFinish = models.DateTimeField( null=True, blank=True)
    SpendToday = models.IntegerField(default = 0)
    SpendSum = models.IntegerField(default = 0)
    RestSum = models.IntegerField(default = 0)
    AvaibleSumToday = models.IntegerField(default = 0)

class Data(models.Model):
    user_ID = models.ManyToManyField (User)
    SpendSum = models.IntegerField(default = 0)
    data = models.DateTimeField( null=True, blank=True)
