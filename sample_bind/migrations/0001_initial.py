# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 02:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField(auto_now_add=True, verbose_name='Submit date')),
                ('receive_date', models.DateTimeField(null=True, verbose_name='Receive date')),
                ('receive_sms', models.BooleanField(default=False, verbose_name='Receive sms send')),
                ('analysis_date', models.DateTimeField(null=True, verbose_name='Analysis date')),
                ('finish_date', models.DateTimeField(null=True, verbose_name='Finish date')),
                ('finish_sms', models.BooleanField(default=False, verbose_name='Finish sms send')),
                ('full_name', models.CharField(max_length=10, verbose_name='Full name')),
                ('status_node', models.CharField(choices=[('SAM', 'Sampling'), ('REC', 'Received'), ('ING', 'Analysing'), ('FIN', 'Finished')], default='SAM', max_length=3, verbose_name='Status')),
            ],
            options={
                'verbose_name_plural': 'binds',
                'verbose_name': 'bind',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_code', models.CharField(max_length=12, unique=True, verbose_name='Sample code')),
                ('sold_out', models.BooleanField(default=False, verbose_name='Sold out')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Add date')),
                ('sold_date', models.DateTimeField(null=True, verbose_name='Sold date')),
            ],
            options={
                'verbose_name_plural': 'codes',
                'verbose_name': 'code',
            },
        ),
        migrations.AddField(
            model_name='bind',
            name='code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sample_bind.Code', verbose_name='Sample code'),
        ),
        migrations.AddField(
            model_name='bind',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
