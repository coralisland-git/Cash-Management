# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-27 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemo', '0014_reconkeys_kt_bill_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='batch_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]