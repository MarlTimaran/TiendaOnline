# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0004_delete_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdescription',
            name='Seller_Username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
