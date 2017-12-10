# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('news_title', models.CharField(max_length=255, verbose_name='Title')),
                ('news_description', models.TextField(max_length=1000, verbose_name='Description')),
                ('news_image', models.ImageField(upload_to='images/news/', verbose_name='Images')),
                ('news_video', models.FileField(upload_to='video/news/', verbose_name='Video')),
                ('news_document', models.FileField(null=True, upload_to='files/news/', verbose_name='Document')),
            ],
            options={
                'verbose_name': 'New',
            },
        ),
    ]
