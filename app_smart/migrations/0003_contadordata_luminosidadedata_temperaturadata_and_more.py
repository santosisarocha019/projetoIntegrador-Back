# Generated by Django 5.0.6 on 2024-05-22 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0002_rename_latitute_sensor_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContadorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_smart.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='LuminosidadeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_smart.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='TemperaturaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_smart.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='UmidadeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_smart.sensor')),
            ],
        ),
    ]
