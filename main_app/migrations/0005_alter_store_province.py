# Generated by Django 5.0 on 2023-12-13 18:06

import localflavor.ca.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_store_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='province',
            field=localflavor.ca.models.CAProvinceField(default='ON', max_length=2),
        ),
    ]