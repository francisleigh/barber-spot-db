# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180910_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chair',
            name='shop',
        ),
        migrations.AlterField(
            model_name='shop',
            name='chairs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Chair'),
        ),
    ]