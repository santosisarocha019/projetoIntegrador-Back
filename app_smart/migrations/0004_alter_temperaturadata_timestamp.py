# Generated by Django 5.0.6 on 2024-05-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0003_contadordata_luminosidadedata_temperaturadata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturadata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]