# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20161203_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
