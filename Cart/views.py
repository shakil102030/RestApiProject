from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import CartItemSerializer
from .models import CartItem, Cart
from Product.models import Food
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status



class CartItemAPIView(APIView):
    def get(self, request, format=None):
        """current_user = request.user
        cart = get_object_or_404(Cart, user_id=current_user.id)
        food = get_object_or_404(Food, food_id = id)
        result = CartItem.objects.get(cart=cart, food=food)
        result.quantity += 1
        result.save()"""
        result = CartItem.objects.all()
        serialize = CartItemSerializer(result, many = True)
        return Response(serialize.data, status=status.HTTP_201_CREATED)


class CartItemDeleteAPIView(APIView):
    def get(self, request, format=None):
            #cart_item = self.get_object()
            current_user = request.user
            cart = get_object_or_404(Cart, user_id=current_user.id)
            food = get_object_or_404(Food, food_id = id)
            result = CartItem.objects.get(cart=cart, food=food)
            if cart_item.cart.user != request.user:
                raise PermissionDenied("Sorry this cart not belong to you")
            cart_item.delete()
            return Response(
                {"detail": _("your item has been deleted.")},
                status=status.HTTP_204_NO_CONTENT,
            )
            