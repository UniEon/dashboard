# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_s_notify'),
    ]

    operations = [
        migrations.AddField(
            model_name='q_notify',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 11, 19, 21, 1, 19, 379690, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s_notify',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 11, 19, 21, 1, 52, 119830, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
