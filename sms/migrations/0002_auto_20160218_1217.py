# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='mobile_phone',
            field=models.CharField(verbose_name='Telephone number', max_length=11),
        ),
    ]
