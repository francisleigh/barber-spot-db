# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_auto_20180917_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='shop_id',
            field=models.ForeignKey(db_column='shop_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
    ]
