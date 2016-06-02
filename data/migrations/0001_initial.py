# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-01 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FboMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitation_type', models.CharField(choices=[(b'PRESOL', b'Pre-Solicitation'), (b'COMB', b'Combined Synopsis/Solicitation'), (b'SS', b'Sources Sought'), (b'MOD', b'Modification/Amendment/Cancel'), (b'SUR', b'Sale of Surplus Property'), (b'NOTICE', b'Special Notice'), (b'FORGOVSTD', b'Foreign Government Standard'), (b'AWDNTC', b'Award Notice'), (b'JST', b'Justification and Approval'), (b'BUNDLE', b'Intent to Bundle Requirements'), (b'FAIR', b'Fair Opportunity / Limited Sources Justification')], max_length=20)),
                ('date', models.DateField()),
                ('year', models.IntegerField()),
                ('agency', models.CharField(max_length=80)),
                ('office', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('zip_code', models.CharField(max_length=15)),
                ('class_code', models.CharField(max_length=10)),
                ('naics', models.CharField(max_length=10)),
                ('office_address', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('solnbr', models.CharField(max_length=20)),
                ('response_date', models.DateField()),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('setaside', models.CharField(max_length=15)),
                ('pop_country', models.CharField(max_length=50)),
                ('pop_address', models.CharField(max_length=100)),
            ],
        ),
    ]
