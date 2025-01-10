from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE) #category.products
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #(auto_now_add) means, the product can be created multiple times
    updated_at = models.DateTimeField(auto_now=True) #(auto_now) means it is updated and can be updated once when creating an instance
    created_by = models.ForeignKey(User, related_name='products_created', on_delete=models.SET_NULL, null=True) #users.products
    updated_by = models.ForeignKey(User, related_name='products_updated', on_delete=models.SET_NULL, null=True)
    deleted_by = models.ForeignKey(User, related_name='products_deleted', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    view_count = models.PositiveIntegerField(default=0)  # Field to track the number of views

    def __str__(self):
        return self.name

    def reduce_stock(self, quantity):
        """
        Reduce stock when a product is purchased or reserved.
        """
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock available")
        
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating out of 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Image for {self.product.name}'
    
#WishList Model
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'wishlist for {self.product.name}'

#Discount Model
class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percentage = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.product.name} - {self.discount_percentage}% off'

