# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20170208_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
