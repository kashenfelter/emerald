# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-03 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbo', '0005_auto_20160903_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbomaster',
            name='agency',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fbomaster',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fbomaster',
            name='office',
            field=models.CharField(max_length=200),
        ),
    ]