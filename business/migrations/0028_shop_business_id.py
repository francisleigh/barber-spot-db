# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0027_auto_20180917_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='business_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Business'),
        ),
    ]
