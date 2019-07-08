# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-07-01 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]
