# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20150419_2040'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=set([('selected', 'its_date')]),
        ),
    ]
