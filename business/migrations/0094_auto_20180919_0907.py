# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 09:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0093_auto_20180919_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 26, 9, 7, 27, 543341), null=True),
        ),
    ]