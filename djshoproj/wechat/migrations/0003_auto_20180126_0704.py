# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_auto_20180126_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
