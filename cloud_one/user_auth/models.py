from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Account(models.Model):
    EN = 'en'
    KR = 'kr'
    CN = 'cn'
    LANGUAGE_CHOICES = ((EN, 'English'), (KR, 'Korean'), (CN, 'Chinese'))

    LVL1 = 1
    LVL2 = 2
    ACCOUNT_LEVELS = ((LVL1, 'level_1'),(LVL2, 'level_2'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null= True)
    description = models.TextField(max_length=255, blank= True)
    website = models.URLField(null=True)
    user_level = models.CharField(max_length=10, choices=ACCOUNT_LEVELS, default=LVL1)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=EN)
    deleted_date = models.TextField(null=True)



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Account.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()