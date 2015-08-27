from django.db import models

# Create your models here.

# Generating User Tokens
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)

# custom fields for User
from mongoengine.fields import ListField
from mongoengine.django.auth import User

class User(User):
    """Extend Mongo Engine User model"""
    #foo = ListField(default=[])
    firstname = StringField()
    lastname = StringField()