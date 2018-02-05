# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='message_weather',
        ),
        migrations.AddField(
            model_name='chat',
            name='weather_humidity',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='chat',
            name='weather_img',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='chat',
            name='weather_pressure',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='chat',
            name='weather_temp',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='chat',
            name='weather_temp_min',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='chat',
            name='weather_wind',
            field=models.CharField(default='', max_length=20),
        ),
    ]