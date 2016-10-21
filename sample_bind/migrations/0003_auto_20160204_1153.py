# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_bind', '0002_remove_bind_relation_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bind',
            name='status_date',
        ),
        migrations.AddField(
            model_name='bind',
            name='analysis_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='bind',
            name='finish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='bind',
            name='receive_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bind',
            name='status_node',
            field=models.CharField(choices=[('SAM', 'Sampling'), ('REC', 'Received'), ('ING', 'Analysing'), ('FIN', 'Finished')], max_length=3, default='SAM'),
        ),
        migrations.AlterField(
            model_name='code',
            name='sample_code',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
