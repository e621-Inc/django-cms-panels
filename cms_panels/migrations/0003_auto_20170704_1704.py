# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms_panels', '0002_auto_20170704_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='panelinfo',
            name='body',
            field=models.TextField(blank=True, default='', verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='panelinfo',
            name='filer_icon',
            field=filer.fields.file.FilerFileField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='Icon'),
        ),
    ]
