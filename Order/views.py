from django.shortcuts import render
from .models import Order, OrderItem
from .serializers import OrderListSerializer, OrderItemSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView

class OrderListAPIView(APIView):
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class CheckoutAPIView(APIView):
    def post(self, request):
        serializer = OrderListSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user, paid_amount=paid_amount)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



