# Generated by Django 5.0 on 2024-06-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_shipment_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='is_delivered',
            field=models.BooleanField(default=True),
        ),
    ]