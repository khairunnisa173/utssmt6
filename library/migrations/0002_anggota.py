# Generated by Django 5.0.4 on 2024-05-07 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField(max_length=255)),
                ('no_telp', models.CharField(max_length=12, validators=[django.core.validators.MaxLengthValidator(12)])),
                ('email', models.EmailField(max_length=254)),
                ('tanggal_lahir', models.DateField()),
                ('tanggal_bergabung', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
