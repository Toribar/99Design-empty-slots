# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0005_auto_20160127_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 27, 17, 42, 57, 957343, tzinfo=utc)),
        ),
    ]
