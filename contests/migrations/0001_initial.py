# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_date', models.DateTimeField(default=datetime.datetime(2016, 2, 21, 17, 55, 45, 863335, tzinfo=utc), verbose_name='Start Date')),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
    ]
