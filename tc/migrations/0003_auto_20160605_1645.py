# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0002_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1024, blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('step', models.CharField(max_length=15, blank=True)),
                ('session', models.ForeignKey(to='tc.TestSession')),
            ],
        ),
        migrations.AlterField(
            model_name='media',
            name='upload',
            field=models.FileField(upload_to=b'images/'),
        ),
    ]
