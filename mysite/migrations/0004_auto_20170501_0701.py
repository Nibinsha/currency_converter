# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20170501_0700'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='curncy',
            new_name='currency',
        ),
    ]
