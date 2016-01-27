# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_remove_contests_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contests',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='contests',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 27, 15, 33, 40, 791492, tzinfo=utc)),
        ),
    ]
