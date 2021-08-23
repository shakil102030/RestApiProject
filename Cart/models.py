from django.db import models
from Product.models import Food
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Cart: " + str(self.id)
    


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=1)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


    
    

   

