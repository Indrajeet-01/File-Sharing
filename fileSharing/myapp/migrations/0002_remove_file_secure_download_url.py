# Generated by Django 5.0.1 on 2024-01-31 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='secure_download_url',
        ),
    ]
