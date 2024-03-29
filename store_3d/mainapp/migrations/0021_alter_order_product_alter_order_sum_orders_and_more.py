# Generated by Django 5.0.3 on 2024-03-25 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='mainapp.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sum_orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sum_orders_orders', to='mainapp.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]