# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-10 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200110_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phoneNumber',
        ),
    ]