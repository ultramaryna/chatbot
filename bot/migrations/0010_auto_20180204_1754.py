# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_auto_20180116_1713'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='chat',
            name='message_weather',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='user_lat',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='user_lon',
            field=models.CharField(default='', max_length=30),
        ),
    ]