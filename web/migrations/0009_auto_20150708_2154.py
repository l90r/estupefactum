# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20150708_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='its_date',
            field=models.DateField(null=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=set([]),
        ),
    ]
