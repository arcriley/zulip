# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-28 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0004_licenseledger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerplan',
            old_name='next_billing_date',
            new_name='next_invoice_date',
        ),
        migrations.RemoveField(
            model_name='customerplan',
            name='billed_through',
        ),
        migrations.AddField(
            model_name='customerplan',
            name='invoiced_through',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='corporate.LicenseLedger'),
        ),
        migrations.AddField(
            model_name='customerplan',
            name='invoicing_status',
            field=models.SmallIntegerField(default=1),
        ),
    ]
