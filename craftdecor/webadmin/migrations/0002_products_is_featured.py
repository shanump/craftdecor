# Generated by Django 4.2.13 on 2024-05-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
