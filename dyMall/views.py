from dyMall.models import Kategori, Produk, PenilaianProduk, Toko
from dyMall.serializers import KategoriSerializer, ProdukSerializer, PenilaianProdukSerializer, TokoSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class KategoriList(generics.ListCreateAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class KategoriDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Kategori.objects.get(pk=pk)
        except Kategori.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        kategori = self.get_object(pk)
        serializer = KategoriSerializer(kategori)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        kategori = self.get_object(pk)
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        kategori = self.get_object(pk)
        kategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Produk.objects.get(pk=pk)
        except Produk.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        produk = self.get_object(pk)
        produk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PenilaianProdukList(generics.ListCreateAPIView):
    queryset = PenilaianProduk.objects.all()
    serializer_class = PenilaianProdukSerializer

class PenilaianProdukDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return PenilaianProduk.objects.get(pk=pk)
        except PenilaianProduk.DoesNotExist:
            raise Http404
        
    def delete(self, request, pk, format=None):
        penilaianproduk = self.get_object(pk)
        penilaianproduk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TokoList(generics.ListCreateAPIView):
    queryset = Toko.objects.all()
    serializer_class = TokoSerializer