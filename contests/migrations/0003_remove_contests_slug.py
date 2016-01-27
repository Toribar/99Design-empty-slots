# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_contests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contests',
            name='slug',
        ),
    ]
