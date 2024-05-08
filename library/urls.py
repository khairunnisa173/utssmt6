from django.urls import path 
from library.views import PerpusList
from library.views import AnggotaList
from library.views import BukuList, BukuDetail
from library.views import PeminjamanList, PeminjamanDetail

urlpatterns = [
    path('perpus/', PerpusList.as_view()),
    path('anggota/', AnggotaList.as_view()),
    path('buku/', BukuList.as_view()),
    path('buku/<int:pk>/', BukuDetail.as_view(),name='buku-detail'),
    path('peminjaman/', PeminjamanList.as_view()),
    path('peminjaman/<int:pk>/', PeminjamanDetail.as_view(),name='peminjaman-detail'),
]
