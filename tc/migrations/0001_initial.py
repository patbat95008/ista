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
                ('user', models.CharField(max_length=50)),
                ('package_type', models.CharField(default=b'STANDARD', max_length=9, choices=[(b'STANDARD', b'Standard'), (b'SMALL', b'Small'), (b'FLAT', b'Flat'), (b'ELONGATED', b'Elongated')])),
                ('test', models.CharField(max_length=10)),
            ],
        ),
    ]
