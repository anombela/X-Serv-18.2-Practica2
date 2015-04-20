# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_auto_20150420_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='url',
            new_name='larga',
        ),
        migrations.AddField(
            model_name='url',
            name='corta',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
