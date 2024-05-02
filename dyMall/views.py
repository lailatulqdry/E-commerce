from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Kategori
from .serializers import KategoriSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def kategori_list(request, format=None):
    print("j")
    if request.method == 'GET':
        kategori = Kategori.objects.all()
        serializer = KategoriSerializer(kategori, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class KategoriList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        kategori = Kategori.objects.all()
        serializer = KategoriSerializer(kategori, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class KategoriDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [permissions.AllowAny]
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