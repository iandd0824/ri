from django.db import models

# Create your models here.

# Generating User Tokens
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from mongoengine import *

#from django.contrib.auth.models import AbstractBaseUser

#class MyUser(AbstractBaseUser):
#    username = StringField(max_length=120, unique=True)
#    email = StringField(max_length=254, unique=True)
 
#    USERNAME_FIELD = 'email'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# custom fields for User
from mongoengine.fields import ListField
from mongoengine.django.auth import User

class User(User):
    """Extend Mongo Engine User model"""
    #foo = ListField(default=[])
    username = StringField(max_length=120, unique=True)
    firstname = StringField()
    lastname = StringField()


    # code to hash the password
    #user.set_password(self.cleaned_data["password"])

# Mongo token
# https://gist.github.com/RockingRolli/79ceab04adb72c106cd6#file-models-py

import binascii
import os
from django.conf import settings
from django.utils.timezone import now
from mongoengine import Document, StringField, ReferenceField
from mongoengine.fields import DateTimeField

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.user')


class MongoToken(Document):
    key = StringField(max_length=44)
    user = ReferenceField('User', required=True)
    created = DateTimeField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        if not self.key:
            self.key = self.generate_key()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()

        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(22)).decode()

    def __unicode__(self):
        return self.key