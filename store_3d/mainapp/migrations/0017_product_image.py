# Generated by Django 5.0.3 on 2024-03-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_cart_user_alter_order_at_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=0, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]
