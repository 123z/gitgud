# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AusCities', '0004_auto_20170919_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collegedepartments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'collegedepartments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Industrytypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industrytype', models.CharField(blank=True, db_column='industryType', max_length=45, null=True)),
            ],
            options={
                'db_table': 'industrytypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationid', models.AutoField(db_column='locationID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='phoneNumber', max_length=45, null=True)),
                ('emailaddress', models.CharField(blank=True, db_column='emailAddress', max_length=80, null=True)),
                ('locationtype', models.CharField(blank=True, db_column='locationType', max_length=10, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]