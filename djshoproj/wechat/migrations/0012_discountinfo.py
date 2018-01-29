# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 05:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wechat', '0011_delete_discountinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('lkurl', models.CharField(max_length=500)),
                ('imgurl', models.CharField(max_length=500)),
                ('keywords', models.CharField(max_length=300)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]