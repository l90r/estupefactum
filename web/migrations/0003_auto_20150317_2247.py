# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150314_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='its_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
