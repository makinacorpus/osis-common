# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-27 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osis_common', '0002_documentfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentfile',
            name='description',
            field=models.CharField(choices=[('ID_CARD', 'identity_card'), ('LETTER_MOTIVATION', 'letter_motivation'), ('ID_PICTURE', 'id_picture')], default='LETTER_MOTIVATION', max_length=50),
        ),
    ]
