from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from . import models


@admin.register(models.User)
class UserAdmin(AuthUserAdmin):
    save_on_top = True
