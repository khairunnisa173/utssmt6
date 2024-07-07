from rest_framework import serializers
from .models import Perpus
from .models import Anggota
from .models import Buku
from .models import PengembalianBuku
from django.contrib.auth.models import User

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

class PengembalianBukuSerializer(serializers.ModelSerializer):
    denda = serializers.SerializerMethodField()

    class Meta:
        model = PengembalianBuku
        fields = ["id", "buku", "pengguna", "tanggal_pinjam", "tanggal_kembali", "tanggal_jatuh_tempo", "denda_per_hari", "status", "denda"]

    def get_denda(self, obj):
        return obj.hitung_denda()

class UserSerializer(serializers.ModelSerializer):
    pengembalianbuku=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pengembalianbuku-detail'
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'pengembalianbuku']