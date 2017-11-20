# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0010_q_notify'),
    ]

    operations = [
        migrations.CreateModel(
            name='s_notify',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Actor', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='s_activities')),
                ('Object', models.ForeignKey(to='dashboard.Story', related_name='s_notif')),
                ('Target', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='s_events')),
            ],
        ),
    ]
