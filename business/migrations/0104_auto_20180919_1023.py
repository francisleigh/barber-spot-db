# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 10:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0103_auto_20180919_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopdaytrade',
            name='day',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 26, 10, 23, 54, 871186), null=True),
        ),
    ]