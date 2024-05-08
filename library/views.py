from rest_framework import generics
from library.models import Perpus
from library.serializers import PerpusSerializer
from library.models import Anggota
from library.serializers import AnggotaSerializer
from library.models import Buku
from library.serializers import BukuSerializer
from library.models import Peminjaman
from library.serializers import PeminjamanSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PerpusList(generics.ListCreateAPIView):
    queryset = Perpus.objects.all()
    serializer_class = PerpusSerializer

class AnggotaList(generics.ListCreateAPIView):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer

class BukuList(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class PeminjamanList(generics.ListCreateAPIView):
    queryset = Peminjaman.objects.all()
    serializer_class = PeminjamanSerializer


class BukuDetail(APIView):
    def get_object(self, pk):
        try:
            return Buku.objects.get(pk=pk)
        except Buku.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        buku = self.get_object(pk)
        serializer = BukuSerializer(buku,context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        buku = self.get_object(pk)
        serializer = BukuSerializer(buku, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        buku = self.get_object(pk)
        buku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PeminjamanDetail(APIView):
    def get_object(self, pk):
        try:
            return Peminjaman.objects.get(pk=pk)
        except Peminjaman.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        peminjaman = self.get_object(pk)
        serializer = PeminjamanSerializer(peminjaman, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        peminjaman = self.get_object(pk)
        serializer = PeminjamanSerializer(peminjaman, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        peminjaman= self.get_object(pk)
        peminjaman.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)