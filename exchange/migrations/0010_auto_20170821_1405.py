# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-21 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0009_auto_20170821_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='walletFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walletFrom', to='exchange.Wallets'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='walletTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walletTo', to='exchange.Wallets'),
        ),
    ]
