# Generated by Django 4.2.13 on 2024-05-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webadmin', '0003_products_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tag',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
