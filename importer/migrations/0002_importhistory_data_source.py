# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-23 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importhistory',
            name='data_source',
            field=models.CharField(default='test', max_length=10),
            preserve_default=False,
        ),
    ]