from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    author = models.ForeignKey(User)
    content = models.CharField(max_length=512)
    created = models.DateTimeField()
    selected = models.BooleanField(default=False)
    its_date = models.DateField(null=True)
    def __str__(self):
        return self.content

class Date(models.Model):
    WORK_DAY = 0
    WEEKEND = 1
    BANK_HOLIDAY = 2
    OTHER = 3

    date_choices = (
        (WORK_DAY, 'Normal work day'),
        (WEEKEND, 'Weekend'),
        (BANK_HOLIDAY, 'Bank holiday'),
        (OTHER, 'Other non-working day'),
    )

    date = models.DateField()
    date_type = models.IntegerField(max_length=1, choices=date_choices)
    description = models.CharField(max_length=512)
    
    def __str__(self):
        return str(self.date)
