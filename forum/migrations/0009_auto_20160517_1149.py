# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20160514_2243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('sticky', 'created_date')},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AddField(
            model_name='post',
            name='sticky',
            field=models.BooleanField(default=False),
        ),
    ]
