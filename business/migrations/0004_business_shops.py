# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_remove_business_shops'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='shops',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Shop'),
        ),
    ]
