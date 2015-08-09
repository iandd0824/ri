#from django.db import models

from mongoengine import *


# Create your models here.
class Restaurant(Document):
    #def __init__(self, id, name, address):
    #    self.id = id
    #    self.name = name
    #    self.address = address
    id = StringField(max_length=200)
    name = StringField(max_length=200)
    address = StringField(max_length=200)