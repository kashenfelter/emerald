# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='job_title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
