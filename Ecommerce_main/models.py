from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.FloatField(null=True)
    product_quantity = models.IntegerField(null=True)
    product_size = models.CharField(max_length=5)
    product_color = models.CharField(max_length=10)
    product_image = models.ImageField(null=True, blank=True, upload_to='images/')
    product_catagories = models.CharField(max_length=10, null=True)
    # Removed the redundant ManyToManyField for comments

    def total_comments(self):
        return self.comments.count()  # Use the reverse relation from the Comment model

    def __str__(self):
        return self.product_name

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Other comment fields

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.product_name}"
    def get_full_name(self):
     return f"{self.user.first_name} {self.user.last_name}"