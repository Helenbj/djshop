# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 01:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0007_discountinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountinfo',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]