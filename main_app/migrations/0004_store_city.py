# Generated by Django 5.0 on 2023-12-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_store_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.CharField(default='Toronto', max_length=50),
        ),
    ]
