from rest_framework import serializers
from .models import  *

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','category', 'status', 'quen')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'desc')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product', 'name', 'slug','desc','price')

class CostumUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostumUser
        fields = ('id','fullnamne', 'email', 'phone_number','address')

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ('id','custmuser', 'product', 'totol_price')

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_photo
        fields = ('id','product', 'thumb', 'lorg_pc')

