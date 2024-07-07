from django.urls import path, include
from library.views import PerpusList
from library.views import AnggotaList
from library.views import BukuList, BukuDetail
from library.views import PengembalianBukuList, PengembalianBukuDetail
from library.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('perpus/', PerpusList.as_view()),
    path('anggota/', AnggotaList.as_view()),
    path('buku/', BukuList.as_view()),
    path('buku/<int:pk>/', BukuDetail.as_view(),name='buku-detail'),
    path('pengembalianbuku/', PengembalianBukuList.as_view()),
    path('pengembalianbuku/<int:pk>/', PengembalianBukuDetail.as_view(),name='pengembalianbuku-detail'),
    path('', include(router.urls)),
]
