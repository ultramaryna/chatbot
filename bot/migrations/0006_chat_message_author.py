# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-13 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20180113_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='message_author',
            field=models.CharField(default='B', max_length=1),
        ),
    ]