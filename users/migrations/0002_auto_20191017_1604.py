# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-17 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthDate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='homeAddress',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phoneNumber',
        ),
    ]