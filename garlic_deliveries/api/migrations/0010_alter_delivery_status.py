# Generated by Django 5.1.7 on 2025-03-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_warhouse_id_delivery_delivery_id_from_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.CharField(choices=[('pending', 'Gaida piegādes apstiprināšanu'), ('processing', 'Apstrādē pie piegādātāja'), ('shipped', 'Tiek piegādāts'), ('delivered', 'Piegādāts'), ('cancelled', 'Piegāde atcelta')], default='pending', max_length=20),
        ),
    ]
