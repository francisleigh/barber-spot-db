# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 10:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0101_auto_20180919_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='shops',
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 26, 10, 5, 35, 152892), null=True),
        ),
    ]
