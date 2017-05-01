# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='currency_input',
            field=models.IntegerField(default=1),
        ),
    ]
