# Generated by Django 5.0.6 on 2024-05-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0004_alter_temperaturadata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luminosidadedata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]