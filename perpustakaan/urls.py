from django.contrib import admin
from django.urls import path
from . import views  # Pastikan impor views.py yang benar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perpus/<int:pk>/', views.perpus),
    path('perpus/', views.perpusHome),
    # Tambahkan rute lain di sini jika diperlukan
]
