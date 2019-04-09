# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0207_multiuseinvite_invited_as'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='night_logo_source',
            field=models.CharField(choices=[('D', 'Default to Zulip'), ('U', 'Uploaded by administrator')], default='D', max_length=1),
        ),
        migrations.AddField(
            model_name='realm',
            name='night_logo_version',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
