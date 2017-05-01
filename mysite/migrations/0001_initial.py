# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency_from', models.CharField(max_length=50)),
                ('currency_to', models.CharField(max_length=50)),
                ('currency_input', models.IntegerField(default=b'')),
            ],
        ),
    ]
