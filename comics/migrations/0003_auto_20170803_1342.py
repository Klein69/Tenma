# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-03 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_auto_20170802_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name_plural': 'Roles'},
        ),
        migrations.AddField(
            model_name='issue',
            name='leaf',
            field=models.PositiveSmallIntegerField(blank=True, default=1, editable=False),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Unread'), (1, 'Partially read'), (2, 'Completed')], default=0, verbose_name='Status'),
        ),
    ]