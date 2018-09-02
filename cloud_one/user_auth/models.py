from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

import os
import uuid
from cloud_one import settings


class UserJWTSecret(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jwt_secret')
    jwt_secret = models.UUIDField(default=uuid.uuid4)


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

# NOTE: Helper function to get the jwt token
def jwt_get_secret_key(user):
    return user.jwt_secret
