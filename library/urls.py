from django.urls import path 
from library.views import PerpusList

urlpatterns = [
    path('perpus/', PerpusList.as_view()),
]
