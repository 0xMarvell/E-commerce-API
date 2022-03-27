from rest_framework import serializers
from products.models import *

class CategorySerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'
        model = Category


class BooksSerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'
        model = Books


class HeadphonesSerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'
        model = Headphones
