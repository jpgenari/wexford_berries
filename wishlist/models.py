from django.db import models
from profiles.models import UserProfile
from products.models import Product

# Create your models here.

class Wishlist(models.Model):
    """
    Wishlist models to store users wishlist products
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name="user_wishlist")
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name
