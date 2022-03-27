from rest_framework import generics
from products.models import *
from .serializers import *


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListBooks(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class DetailBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer 


class ListHeadphones(generics.ListCreateAPIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesSerializer


class DetailHeadphones(generics.RetrieveUpdateDestroyAPIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesSerializer 
