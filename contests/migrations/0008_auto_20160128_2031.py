# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0007_auto_20160127_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 28, 20, 31, 13, 925771, tzinfo=utc)),
        ),
    ]
