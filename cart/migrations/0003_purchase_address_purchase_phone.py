# Generated by Django 5.0.7 on 2024-08-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
