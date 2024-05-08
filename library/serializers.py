from rest_framework import serializers
from .models import Perpus
from .models import Anggota
from .models import Buku
from .models import Peminjaman

class PerpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perpus
        fields = ["id", "nama", "alamat"]

class AnggotaSerializer(serializers.ModelSerializer):
    peminjaman_anggota = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='peminjaman-detail'
    )
    class Meta:
        model = Anggota
        fields = ["id", "nama", "alamat", "no_telp", "email", "tanggal_lahir", "tanggal_bergabung", 'peminjaman_anggota']

class BukuSerializer(serializers.ModelSerializer):
    peminjaman = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='peminjaman-detail'
    )
    class Meta:
        model = Buku
        fields = ["id", "judul", "kode", "genre", 'peminjaman']

class PeminjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peminjaman
        fields = ["id", "buku", "anggota", "tanggal_pinjam", "tanggal_pengembalian", "denda", "status"]