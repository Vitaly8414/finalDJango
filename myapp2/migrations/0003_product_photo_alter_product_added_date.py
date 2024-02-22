# Generated by Django 5.0.2 on 2024-02-07 04:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_alter_client_email_alter_client_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
