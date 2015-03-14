from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=512)
    created = models.DateTimeField()
    selected = models.BooleanField(default=False)
    its_date = models.DateField()

class Date(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=512)

