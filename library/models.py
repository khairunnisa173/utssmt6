from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class Perpus(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField(max_length=255)
    
    def __str__(self):
        return self.nama
    
class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField(max_length=255)
    no_telp = models.CharField(max_length=12, validators=[MaxLengthValidator(12)])
    email = models.EmailField()
    tanggal_lahir = models.DateField()
    tanggal_bergabung = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama
    
class Buku(models.Model):
    judul = models.CharField(max_length=100)
    kode = models.CharField(max_length=100)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.judul
    
class PengembalianBuku(models.Model):
    STATUS_CHOICES = [
        ('belum_dikembalikan', 'Belum Dikembalikan'),
        ('sudah_dikembalikan', 'Sudah Dikembalikan'),
        ('hilang', 'Hilang'),
        ('rusak', 'Rusak'),
    ]
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField(null=True, blank=True)
    tanggal_jatuh_tempo = models.DateField()
    denda_per_hari = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='belum_dikembalikan')

    def hitung_denda(self):
        if self.status == 'sudah_dikembalikan' and self.tanggal_kembali and self.tanggal_kembali > self.tanggal_jatuh_tempo:
            delta = self.tanggal_kembali - self.tanggal_jatuh_tempo
            return delta.days * self.denda_per_hari
        return 0.00

    def _str_(self):
        return f"{self.buku.judul} dipinjam oleh {self.pengguna.user.username}"







