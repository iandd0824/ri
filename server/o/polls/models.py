from django.db import models

# Create your models here.
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')


#class Choice(models.Model):
#    question = models.ForeignKey(Question)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)


from mongoengine import *

class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)

class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))

    meta = {
        'indexes': [
            'question', 
            ('pub_date', '+question')
        ]
    }

class Lady(Document):
    firstname = StringField()
    lastname = StringField()

# Tutorial 4
# owner = models.ForeignKey('auth.User', related_name='ladys')
# highlighted = models.TextField()

# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

# def save(self, *args, **kwargs):
#     """
#     Use the `pygments` library to create a highlighted HTML
#     representation of the code snippet.
#     """
#     lexer = get_lexer_by_name(self.language)
#     linenos = self.linenos and 'table' or False
#     options = self.title and {'title': self.title} or {}
#     formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
#     self.highlighted = highlight(self.code, lexer, formatter)
#     super(Snippet, self).save(*args, **kwargs)

# Mongoengine User model

from mongoengine.fields import ListField
from mongoengine.django.auth import User

class User(User):
    """Extend Mongo Engine User model"""
    foo = ListField(default=[])
    name = StringField()


# Generating Tokens
#from django.conf import settings
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from rest_framework.authtoken.models import Token

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)