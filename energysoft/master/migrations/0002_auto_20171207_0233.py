# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='active_status',
            field=models.BooleanField(default=False, verbose_name='Active Status'),
        ),
    ]
