# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20180913_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='time_slots',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.TimeSlot'),
        ),
    ]