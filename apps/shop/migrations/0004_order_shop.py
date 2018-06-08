# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-08 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180607_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Shop', verbose_name='属性ID'),
            preserve_default=False,
        ),
    ]
