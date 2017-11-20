# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20171120_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.ForeignKey(related_name='posted_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
