# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0001_initial'),
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
