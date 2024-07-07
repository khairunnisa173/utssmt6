from rest_framework import generics
from library.models import Perpus
from library.serializers import PerpusSerializer
from library.models import Anggota
from library.serializers import AnggotaSerializer
from library.models import Buku
from library.serializers import BukuSerializer
# from library.models import Peminjaman
# from library.serializers import PeminjamanSerializer
from library.models import PengembalianBuku
from library.serializers import PengembalianBukuSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from library.serializers import UserSerializer

class PerpusList(generics.ListCreateAPIView):
    queryset = Perpus.objects.all()
    serializer_class = PerpusSerializer

class AnggotaList(generics.ListCreateAPIView):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer

class BukuList(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class PengembalianBukuList(generics.ListCreateAPIView):
    queryset = PengembalianBuku.objects.all()
    serializer_class = PengembalianBukuSerializer

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
    
class PengembalianBukuDetail(APIView):
    def get_object(self, pk):
        try:
            return PengembalianBuku.objects.get(pk=pk)
        except PengembalianBuku.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pengembalianbuku = self.get_object(pk)
        serializer = PengembalianBukuSerializer(pengembalianbuku, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pengembalianbuku = self.get_object(pk)
        serializer = PengembalianBukuSerializer(pengembalianbuku, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pengembalianbuku= self.get_object(pk)
        pengembalianbuku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer