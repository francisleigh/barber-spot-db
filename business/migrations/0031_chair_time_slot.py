# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0030_auto_20180917_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='chair',
            name='time_slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.TimeSlot'),
        ),
    ]
