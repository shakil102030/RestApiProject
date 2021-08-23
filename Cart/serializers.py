from rest_framework import serializers

from .models import CartItem

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"
        depth = 2