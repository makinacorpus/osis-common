# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('osis_common', '0006_modifications_documentfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfile',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
    ]