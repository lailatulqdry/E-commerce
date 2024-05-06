from rest_framework import serializers
from .models import Kategori, Produk

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = [
            "id",
            "name",
            "harga",
            "deskripsi",
            "gambar", 
            "kategori"
            ]

class KategoriSerializer(serializers.ModelSerializer):
    produk = ProdukSerializer(many=True, read_only=True)
    class Meta:
        model = Kategori
        fields = '__all__'

