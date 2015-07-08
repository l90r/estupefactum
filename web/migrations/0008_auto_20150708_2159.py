# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20150419_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='its_date',
            field=models.DateField(null=True, unique=True),
            preserve_default=True,
        ),
    ]
