from django.db import models

class User(models.Model):
    user_ID = models.ManyToManyField ()
    budget_ID = models.ManyToManyField ()
    email =
    password =
    name = models.CharField( max_length=255, )


class CurrentBudget(models.Model):
    user_ID = models.ManyToManyField ()
    budget_ID = models.ManyToManyField ()
    moneySum = models.IntegerField(default = 0)
    DateOfStart = models.DateTimeField( null=True, blank=True)
    DateOfFinish = models.DateTimeField( null=True, blank=True)
    SpendToday = models.IntegerField(default = 0)
    SpendSum = models.IntegerField(default = 0)
    RestSum = models.IntegerField(default = 0)
    AvaibleSumToday = models.IntegerField(default = 0)

class Data(models.Model):
    user_ID = models.ManyToManyField ()
    SpendSum = models.IntegerField(default = 0)
    data = models.DateTimeField( null=True, blank=True)
