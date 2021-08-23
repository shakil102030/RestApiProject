from rest_framework import serializers
from .models import Order, OrderItem


class OrderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id','first_name','last_name','email','address','postal_code','city','phone','items')

    
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('price','Food','quantity')
