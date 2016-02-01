# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0006_auto_20160127_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 27, 19, 10, 1, 758902, tzinfo=utc)),
        ),
    ]
