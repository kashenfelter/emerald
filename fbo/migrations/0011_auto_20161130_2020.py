# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-30 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbo', '0010_auto_20161130_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbomaster',
            name='office_address',
            field=models.CharField(max_length=400),
        ),
    ]
