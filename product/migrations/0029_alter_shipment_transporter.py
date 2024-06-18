# Generated by Django 5.0 on 2024-06-11 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_remove_shipment_quotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='transporter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transporter_who_accepted_the_shipment', to='product.transporter'),
        ),
    ]