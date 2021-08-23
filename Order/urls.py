from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
#router.register(r'', views.CategoryViewSet)


urlpatterns = [
    path("order", views.OrderListAPIView.as_view()), 
    path('checkout/', views.CheckoutAPIView.as_view()),
]