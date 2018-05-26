# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=255, null=True, blank=True)),
                ('lastname', models.CharField(max_length=255, null=True, blank=True)),
                ('username', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('password', models.CharField(default=b'', max_length=255, null=True, blank=True)),
            ],
        ),
    ]
