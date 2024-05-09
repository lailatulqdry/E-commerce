from django.db import models

# Create your models here.
class Toko(models.Model):
    namatoko = models.CharField(max_length=20)
    alamattoko = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.namatoko

class Kategori(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Produk(models.Model):
    kategori = models.ForeignKey(Kategori, related_name='produk', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='gambar_produk/', null=True, blank=True)

    def __str__(self):
        return self.name

class PenilaianProduk(models.Model):
    produk = models.ForeignKey(Produk, related_name='penilaianproduk', on_delete=models.CASCADE)
    rating = models.IntegerField()
    komentar = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating
