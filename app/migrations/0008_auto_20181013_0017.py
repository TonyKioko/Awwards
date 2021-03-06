# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 21:17
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181012_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
