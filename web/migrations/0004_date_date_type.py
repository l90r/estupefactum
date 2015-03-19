# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150317_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='date_type',
            field=models.IntegerField(max_length=1, default=0, choices=[(0, 'Normal work day'), (1, 'Weekend'), (2, 'Bank holiday'), (3, 'Other non-working day')]),
            preserve_default=False,
        ),
    ]
