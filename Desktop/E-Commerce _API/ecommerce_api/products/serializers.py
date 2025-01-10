from rest_framework import serializers
from .models import Product, Category, Review, ProductImage, Wishlist, Discount
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(category=category, **validated_data)
        return product
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        if category_data:
            category, created = Category.objects.get_or_create(**category_data)
            instance.category = category
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.stock_quantity = validated_data.get('stock_quantity', instance.stock_quantity)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_at', 'updated_at']

#Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user  # Get the current authenticated user
        validated_data['user'] = user
        return super().create(validated_data)

#product Image Serializer
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', 'created_at']

#WishList Serializer
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['user', 'product', 'created_at']

#Discount Serializer
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'product', 'discount_percentage', 'start_date', 'end_date']
