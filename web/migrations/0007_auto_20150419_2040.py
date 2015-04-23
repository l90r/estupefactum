# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20150411_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='content',
            field=models.CharField(max_length=512, unique=True),
            preserve_default=True,
        ),
    ]
