# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 06:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='zip_cide',
            new_name='zip_code',
        ),
    ]