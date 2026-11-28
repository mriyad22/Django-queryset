from django.db import models
from test_query.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_product'
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_order'
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.product.name} x {self.quantity}"


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)