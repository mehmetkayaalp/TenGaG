# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenGag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.RenameField(
            model_name='commentinfo',
            old_name='comment',
            new_name='commentName',
        ),
        migrations.RemoveField(
            model_name='commentinfo',
            name='date',
        ),
    ]
