# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydemo', '0006_auto_20180525_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='batch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydemo.Batch'),
        ),
    ]
