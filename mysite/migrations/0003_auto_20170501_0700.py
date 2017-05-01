# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20170501_0447'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='currency',
            new_name='curncy',
        ),
    ]
