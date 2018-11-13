# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
            preserve_default=False,
        ),
    ]
