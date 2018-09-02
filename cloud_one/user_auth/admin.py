from django.contrib import admin
from user_auth.models import Account, UserJWTSecret
# Register your models here.

admin.site.register(Account)
admin.site.register(UserJWTSecret)

