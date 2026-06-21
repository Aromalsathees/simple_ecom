from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    is_paid = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=255,blank=True)
    razorpay_payment_id = models.CharField(max_length=255,blank=True)
    
class OrderItem(models.Model):

    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product.name