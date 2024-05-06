from django.db import models

# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Produk(models.Model):
    kategori = models.ForeignKey(Kategori, related_name='produk', on_delete=models.CASCADE,)
    name = models.CharField(max_length=20)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='gambar_produk/', null=True, blank=True)

    def __str__(self):
        return self.name
