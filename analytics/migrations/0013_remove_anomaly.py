# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-02 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0012_add_on_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installationcount',
            name='anomaly',
        ),
        migrations.RemoveField(
            model_name='realmcount',
            name='anomaly',
        ),
        migrations.RemoveField(
            model_name='streamcount',
            name='anomaly',
        ),
        migrations.RemoveField(
            model_name='usercount',
            name='anomaly',
        ),
        migrations.DeleteModel(
            name='Anomaly',
        ),
    ]
