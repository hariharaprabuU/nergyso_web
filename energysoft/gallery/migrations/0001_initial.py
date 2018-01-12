# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-10 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('gallery_title', models.CharField(max_length=255, verbose_name='Title')),
                ('gallery_image', models.FileField(upload_to=gallery.models.update_image, verbose_name='Images')),
            ],
            options={
                'verbose_name': 'Gallery',
            },
        ),
    ]
