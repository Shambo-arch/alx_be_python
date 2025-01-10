from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, 
    ProductViewSet, 
    ReviewViewSet, 
    ProductImageViewSet, 
    WishlistViewSet, 
    DiscountViewSet, 
    IncreaseViewCount,
)

# Create a router for automatic URL generation
router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('reviews', ReviewViewSet, basename='review')
router.register('product-images', ProductImageViewSet, basename='product-image')
router.register('wishlists', WishlistViewSet, basename='wishlist')
router.register('discounts', DiscountViewSet, basename='discount')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/increase-view-count/', IncreaseViewCount.as_view(), name='increase-view-count'),
]
