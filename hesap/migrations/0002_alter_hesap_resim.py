# Generated by Django 3.2.8 on 2021-10-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hesap',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
