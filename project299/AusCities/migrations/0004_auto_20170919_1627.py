# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AusCities', '0003_auto_20170919_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=300),
        ),
    ]
