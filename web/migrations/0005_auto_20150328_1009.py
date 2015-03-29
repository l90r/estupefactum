# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_date_date_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
