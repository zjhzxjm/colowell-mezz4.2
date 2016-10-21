# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sample_bind', '0003_auto_20160204_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bind',
            options={'verbose_name': 'bind', 'verbose_name_plural': 'binds'},
        ),
        migrations.AlterModelOptions(
            name='code',
            options={'verbose_name': 'code', 'verbose_name_plural': 'codes'},
        ),
        migrations.AlterField(
            model_name='bind',
            name='analysis_date',
            field=models.DateTimeField(verbose_name='Analysis date', null=True),
        ),
        migrations.AlterField(
            model_name='bind',
            name='code',
            field=models.OneToOneField(verbose_name='Sample code', to='sample_bind.Code'),
        ),
        migrations.AlterField(
            model_name='bind',
            name='finish_date',
            field=models.DateTimeField(verbose_name='Finish date', null=True),
        ),
        migrations.AlterField(
            model_name='bind',
            name='full_name',
            field=models.CharField(verbose_name='Full name', max_length=10),
        ),
        migrations.AlterField(
            model_name='bind',
            name='receive_date',
            field=models.DateTimeField(verbose_name='Receive date', null=True),
        ),
        migrations.AlterField(
            model_name='bind',
            name='status_node',
            field=models.CharField(verbose_name='Status', choices=[('SAM', 'Sampling'), ('REC', 'Received'), ('ING', 'Analysing'), ('FIN', 'Finished')], default='SAM', max_length=3),
        ),
        migrations.AlterField(
            model_name='bind',
            name='submit_date',
            field=models.DateTimeField(verbose_name='Submit date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bind',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='code',
            name='add_date',
            field=models.DateTimeField(verbose_name='Add date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='sample_code',
            field=models.CharField(verbose_name='Sample code', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='sold_date',
            field=models.DateTimeField(verbose_name='Sold date', null=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='sold_out',
            field=models.BooleanField(verbose_name='Sold out', default=False),
        ),
    ]
