# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-09 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0005_auto_20161207_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samrecord',
            name='naics_code_counter',
        ),
        migrations.RemoveField(
            model_name='samrecord',
            name='naics_code_string',
        ),
        migrations.AddField(
            model_name='samrecord',
            name='naics',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]