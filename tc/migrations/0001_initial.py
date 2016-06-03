# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=50)),
                ('user', models.CharField(default=b'anonymous', max_length=50)),
                ('package_type', models.CharField(default=b'standard', max_length=9, choices=[(b'standard', b'standard'), (b'small', b'small'), (b'flat', b'flat'), (b'elongated', b'elongated')])),
                ('test', models.CharField(max_length=10)),
                ('state', models.CharField(default=b'', max_length=15)),
                ('last_step', models.CharField(default=b'', max_length=10)),
            ],
        ),
    ]
