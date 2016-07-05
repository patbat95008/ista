# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload', models.FileField(upload_to=b'uploads/')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('step', models.CharField(max_length=15, blank=True)),
                ('session', models.ForeignKey(to='tc.TestSession')),
            ],
        ),
    ]
