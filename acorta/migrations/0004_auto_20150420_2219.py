# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0003_auto_20150420_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='larga',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='url',
            name='corta',
        ),
    ]
