# Generated by Django 5.1.7 on 2025-03-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='type_amount',
            field=models.JSONField(default=list),
        ),
    ]
