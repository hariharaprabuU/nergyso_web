# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-10 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Department', verbose_name='Department'),
        ),
    ]
