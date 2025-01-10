from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Product, Category, Review, ProductImage, Wishlist, Discount
from .filters import ProductFilter 
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import ProductPagination
from .serializers import (
    ProductSerializer, 
    ProductDetailSerializer, 
    CategorySerializer, 
    ReviewSerializer, 
    ProductImageSerializer, 
    WishlistSerializer, 
    DiscountSerializer,
)

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = ProductFilter  # Use the ProductFilter for filtering
    pagination_class = ProductPagination # Enable pagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Product Image ViewSet
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]

# Wishlist ViewSet
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

# Discount ViewSet
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated]

# Custom View for Increasing Product View Count
class IncreaseViewCount(APIView):
    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.view_count += 1
            product.save()
            return Response({'message': 'View count increased'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
