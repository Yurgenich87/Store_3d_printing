# Generated by Django 5.0.3 on 2024-03-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_user_postal_сode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='postal_сode',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='second_name',
            new_name='postal_code',
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
