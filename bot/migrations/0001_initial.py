# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-06 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('napis_text', models.CharField(max_length=200)),
                ('data_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
