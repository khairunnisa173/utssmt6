# Generated by Django 5.0.4 on 2024-05-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_anggota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='perpus',
            name='no_telp',
        ),
    ]