# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 01:41
from __future__ import unicode_literals

import AusCities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AusCities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('usertype', AusCities.models.EnumField(choices=[('Student', 's'), ('Tourist', 't'), ('Businessman', 'b')])),
            ],
        ),
    ]
