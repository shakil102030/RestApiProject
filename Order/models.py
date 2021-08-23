from django.db import models
from Product.models import Food
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Onshiping', 'Onshiping'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True)
    postal_code = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    paid_amount  = models.FloatField()
    phone = models.CharField(max_length=200, blank=True)
    status = models.CharField(choices=STATUS, max_length=20, default='New')
    ip = models.CharField(max_length=200, blank=True)
    transaction_id = models.CharField(max_length=200, blank=True)
    transaction_image = models.ImageField(upload_to='transac_image/', blank=True)
    adminnote = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.first_name    #self.user.first_name

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.transaction_image.url))
    image_tag.short_description = 'Image'


class OrderItem(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Cancelled', 'Cancelled')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Food = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    slug = models.SlugField(null = True, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Food.title
