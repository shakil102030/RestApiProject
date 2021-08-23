from django.urls import path
from . import views



urlpatterns = [
    #path("cart/<int:id>/", views.CartItemAPIView.as_view()),
    path("cart", views.CartItemAPIView.as_view()),
    path("delete", views.CartItemDeleteAPIView.as_view()),
]