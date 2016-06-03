# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsession',
            name='last_step',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='state',
            field=models.CharField(default=b'', max_length=15),
        ),
    ]
