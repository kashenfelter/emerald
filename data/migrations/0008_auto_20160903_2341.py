# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-03 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20160903_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbomaster',
            name='solnbr',
            field=models.CharField(max_length=100),
        ),
    ]
