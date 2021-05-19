from rest_framework import serializers

from app_administracion.models.blogs import Blog
from app_administracion.models.contacto import Contacto
from app_administracion.models.product import Product, Category, GalleryImgProduct
from app_administracion.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'cover_image', 'more_info', 'description_corta']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class GalleryImgProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImgProduct
        fields = ('id', 'imagen')


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    gallery = GalleryImgProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
