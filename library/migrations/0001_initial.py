# Generated by Django 5.0.4 on 2024-05-07 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField(max_length=255)),
                ('no_telp', models.CharField(max_length=12, validators=[django.core.validators.MaxLengthValidator(12)])),
            ],
        ),
    ]