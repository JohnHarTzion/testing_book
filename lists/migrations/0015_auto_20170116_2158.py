# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0014_auto_20170116_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
    ]