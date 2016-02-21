# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='Start Date', blank=True),
        ),
    ]
