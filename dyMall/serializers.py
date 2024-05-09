from rest_framework import serializers
from .models import Kategori, Produk, PenilaianProduk, Toko


class PenilaianProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenilaianProduk
        fields = [
            "id",
            "produk",
            "rating",
            "komentar",
            "tanggal",
        ]

class ProdukSerializer(serializers.ModelSerializer):
    penilaianproduk = PenilaianProdukSerializer(many=True,  read_only=True)
    class Meta:
        model = Produk
        fields = [
            "id",
            "kategori",
            "name",
            "harga",
            "deskripsi",
            "gambar",
            "penilaianproduk",
        ]

class KategoriSerializer(serializers.ModelSerializer):
    produk = ProdukSerializer(many=True, read_only=True)
    class Meta:
        model = Kategori
        fields = '__all__'

class TokoSerializer(serializers.ModelSerializer):
    kategori = KategoriSerializer(many=True, read_only=True)
    class Meta:
        model = Toko
        fields = [
            "id",
            "namatoko",
            "alamattoko",
            "rating",
            "kategori",
        ]

