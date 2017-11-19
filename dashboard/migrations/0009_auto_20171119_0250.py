# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20171119_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='story',
            name='source',
            field=models.URLField(max_length=250),
        ),
    ]
