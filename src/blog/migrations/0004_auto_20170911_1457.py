# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170911_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
