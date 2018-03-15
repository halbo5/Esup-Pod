# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20180310_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='restrict_access_to_groups',
            field=models.ManyToManyField(blank=True,
                                         help_text='Select one or more groups '
                                         + 'who can access to this video',
                                         to='auth.Group',
                                         verbose_name='Goups'),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=tagging.fields.TagField(blank=True,
                                          help_text='Separate tags with '
                                          + 'spaces, enclose the tags consist '
                                          + 'of several words in quotation '
                                          + 'marks.',
                                          max_length=255, verbose_name='Tags'),
        ),
    ]