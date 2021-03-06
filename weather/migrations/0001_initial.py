# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('rpk', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.CharField(max_length=25)),
                ('r_10m', models.FloatField(blank=True, null=True)),
                ('r_1h', models.FloatField(blank=True, null=True)),
                ('r_3h', models.FloatField(blank=True, null=True)),
                ('r_6h', models.FloatField(blank=True, null=True)),
                ('r_12h', models.FloatField(blank=True, null=True)),
                ('r_24h', models.FloatField(blank=True, null=True)),
                ('r_td', models.FloatField(blank=True, null=True)),
                ('r_yd', models.FloatField(blank=True, null=True)),
                ('r_2d', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Rainfall',
                'verbose_name_plural': 'Rainfalls',
            },
        ),
        migrations.CreateModel(
            name='RainfallStation',
            fields=[
                ('spk', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('sid', models.CharField(max_length=5)),
                ('county', models.CharField(max_length=3)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            options={
                'verbose_name': 'RainfallStation',
                'verbose_name_plural': 'RainfallStations',
            },
        ),
        migrations.AddField(
            model_name='rainfall',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.RainfallStation'),
        ),
    ]
