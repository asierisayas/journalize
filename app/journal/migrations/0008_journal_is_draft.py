# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("journal", "0007_auto_20171005_2024")]

    operations = [
        migrations.AddField(
            model_name="journal",
            name="is_draft",
            field=models.BooleanField(default=True),
        )
    ]
