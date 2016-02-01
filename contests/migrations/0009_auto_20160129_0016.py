# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0008_auto_20160128_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 0, 16, 31, 227756, tzinfo=utc)),
        ),
    ]
