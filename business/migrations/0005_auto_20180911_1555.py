# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_chair_r_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='r_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
    ]