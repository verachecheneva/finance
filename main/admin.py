from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User, CurrentBudget
admin.site.register(User)
admin.site.register(CurrentBudget)


# Register your models here.
