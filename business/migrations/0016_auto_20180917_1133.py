# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0015_auto_20180917_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='chairs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Chair'),
        ),
    ]
