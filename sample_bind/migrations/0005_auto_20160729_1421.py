# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_bind', '0004_auto_20160302_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='bind',
            name='finish_sms',
            field=models.BooleanField(default=False, verbose_name='Finish sms send'),
        ),
        migrations.AddField(
            model_name='bind',
            name='receive_sms',
            field=models.BooleanField(default=False, verbose_name='Receive sms send'),
        ),
    ]
