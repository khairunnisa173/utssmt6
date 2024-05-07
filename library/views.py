from rest_framework import generics
from library.models import Perpus
from library.serializers import PerpusSerializer


class PerpusList(generics.ListCreateAPIView):
    queryset = Perpus.objects.all()
    serializer_class = PerpusSerializer