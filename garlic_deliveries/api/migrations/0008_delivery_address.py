# Generated by Django 5.1.7 on 2025-03-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_delivery_warhouse_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='address',
            field=models.CharField(default='nav vērtības', max_length=255),
            preserve_default=False,
        ),
    ]
