from rest_framework import serializers
from .models import Perpus

class PerpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perpus
        fields = ["id", "title", "content", "published_date"]