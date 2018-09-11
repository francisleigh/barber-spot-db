# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_owner', '0003_auto_20180911_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='chairs',
        ),
        migrations.AddField(
            model_name='shop',
            name='chairs',
            field=models.ManyToManyField(to='business_owner.Chair'),
        ),
    ]