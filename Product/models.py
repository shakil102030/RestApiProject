from django.db import models
#from django.contrib.auth.models import User
from mptt.models import TreeForeignKey
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    categoryThumb = models.ImageField(blank = True, upload_to = 'images/category_thomb/')
    slug = models.SlugField(null = True, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    Status = (
        ('In Stock', 'In Stock'),
        ('Out Stock', 'Out Stock'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #category = TreeForeignKey(Category,  on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    image = models.ImageField(upload_to='food/food_image/', blank=True)
    new_price = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=30, choices=Status)
    is_deleted = models.BooleanField(default=False)
    slug = models.SlugField(null = True, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
