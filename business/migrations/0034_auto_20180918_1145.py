# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 11:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0033_auto_20180918_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openclosetimes',
            name='day_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.TradingTimes'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 11, 45, 45, 890871), null=True),
        ),
        migrations.AlterField(
            model_name='tradingtimes',
            name='monday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='M', to='business.OpenCloseTimes', to_field='day_name'),
        ),
    ]