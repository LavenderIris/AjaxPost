# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxPost', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='content',
            new_name='desc',
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
