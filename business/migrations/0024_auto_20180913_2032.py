# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0023_auto_20180913_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='shop_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Shop'),
        ),
    ]
