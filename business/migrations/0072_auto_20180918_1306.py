# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 13:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0071_auto_20180918_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradetime',
            name='tuesday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.DayTradeTime'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 25, 13, 6, 48, 55747), null=True),
        ),
        migrations.AlterField(
            model_name='tradetime',
            name='monday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='business.DayTradeTime'),
        ),
    ]