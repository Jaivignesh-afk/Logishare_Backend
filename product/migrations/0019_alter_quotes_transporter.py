# Generated by Django 5.0 on 2024-06-03 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_quotes_transporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='transporter',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='transporter_who_gave_quote', to='product.transporter'),
        ),
    ]