# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180910_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chair',
            old_name='duration',
            new_name='duration_weeks',
        ),
    ]
