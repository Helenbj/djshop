# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0003_auto_20180126_0704'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DiscountInfo',
        ),
    ]