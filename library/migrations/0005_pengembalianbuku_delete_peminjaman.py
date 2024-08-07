# Generated by Django 5.0.4 on 2024-07-05 14:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_buku_genre_peminjaman'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PengembalianBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pinjam', models.DateField()),
                ('tanggal_kembali', models.DateField(blank=True, null=True)),
                ('tanggal_jatuh_tempo', models.DateField()),
                ('denda_per_hari', models.DecimalField(decimal_places=2, default=1.0, max_digits=5)),
                ('status', models.CharField(choices=[('belum_dikembalikan', 'Belum Dikembalikan'), ('sudah_dikembalikan', 'Sudah Dikembalikan'), ('hilang', 'Hilang'), ('rusak', 'Rusak')], default='belum_dikembalikan', max_length=20)),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.buku')),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Peminjaman',
        ),
    ]
