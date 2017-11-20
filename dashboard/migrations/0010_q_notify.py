# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0009_auto_20171119_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='q_notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actor', models.ForeignKey(related_name='q_activities', to=settings.AUTH_USER_MODEL)),
                ('Object', models.ForeignKey(related_name='q_notif', to='dashboard.Question')),
                ('Target', models.ForeignKey(related_name='q_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
