# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 13:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20181015_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 13, 53, 45, 937504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='average',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
    ]
