from django.db import models
from django.core.validators import MaxLengthValidator


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

class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE,related_name='peminjaman')
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE, related_name='peminjaman_anggota') 
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_pengembalian = models.DateField(null=True, blank=True)
    denda = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=[('Dipinjam', 'Dipinjam'), ('Dikembalikan', 'Dikembalikan')])

    def _str_(self):
        return self.buku





