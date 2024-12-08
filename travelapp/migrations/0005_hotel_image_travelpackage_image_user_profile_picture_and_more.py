# Generated by Django 5.1.3 on 2024-12-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_hotel_travelpackage_hotels_seasonalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_images/'),
        ),
        migrations.AddField(
            model_name='travelpackage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='travelpackage_images/'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('ESEWA', 'ESEWA'), ('Khalti', 'Khalti'), ('Google Pay', 'Google Pay'), ('Bank Transfer', 'Bank Transfer')], max_length=20),
        ),
    ]
