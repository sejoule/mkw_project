from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
import os
from cloud_one import settings


class Account(models.Model):
    EN = 'en'
    KR = 'kr'
    CN = 'cn'
    LANGUAGE_CHOICES = ((EN, 'English'), (KR, 'Korean'), (CN, 'Chinese'))

    LVL1 = '1'
    LVL2 = '2'
    ACCOUNT_LEVELS = ((LVL1, 'Level_1'), (LVL2, 'Level_2'))



    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True)
    description = models.TextField(max_length=255, blank= True)
    website = models.URLField(null=True, blank= True)
    user_level = models.CharField(max_length=10, choices=ACCOUNT_LEVELS, default=LVL1, blank= True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=EN, blank= True)
    deleted_date = models.TextField(null=True, blank= True)
    avatar = ProcessedImageField(upload_to='avatars',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 80},
                                 null= True, blank=True
                                 )
    def delete_avatar(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.avatar.name))


# class AvatarFile(models.Model):
#     file = models.FileField(blank=True, null=True)
#     user = models.ForeignKey(User, on_delete=CASCADE, null= True) #NOTE the user that uploaded the avatar
#     created_date = models.DateTimeField(null=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Account.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()