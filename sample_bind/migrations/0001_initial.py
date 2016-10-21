# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bind',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('status_date', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=10)),
                ('relation_name', models.CharField(max_length=2, choices=[('ME', 'Self'), ('FA', 'Father'), ('MO', 'Mother'), ('DA', 'Daughter'), ('SO', 'Son'), ('OT', 'Other relatives')])),
                ('status_node', models.CharField(max_length=3, default='SAM', choices=[('SAM', 'Sampling'), ('ING', 'Analysing'), ('FIN', 'Finished')])),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sample_code', models.CharField(unique=True, max_length=10)),
                ('sold_out', models.BooleanField(default=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('sold_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bind',
            name='code',
            field=models.OneToOneField(to='sample_bind.Code'),
        ),
        migrations.AddField(
            model_name='bind',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
