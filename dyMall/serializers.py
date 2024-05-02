from rest_framework import serializers
from .models import Kategori

class KategoriSerializer(serializers.Serializer):
    class Meta:
        model = Kategori
        fields = ["id", "nama"]