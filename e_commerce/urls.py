from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dyMall.views import KategoriList, KategoriDetail, ProdukList, ProdukDetail, PenilaianProdukList, TokoList
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/kategori/', KategoriList.as_view()),
    path('api/kategori/<int:pk>/', KategoriDetail.as_view()),
    path('api/produk/', ProdukList.as_view()),
    path('api/produk/<int:pk>/', ProdukDetail.as_view()),
    path('api/penilaianproduk/', PenilaianProdukList.as_view()),
    path('api/toko/', TokoList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
