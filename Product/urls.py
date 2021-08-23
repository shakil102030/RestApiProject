from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
#router.register(r'', views.CategoryViewSet)


urlpatterns = [
    #path('categorygf', include(router.urls))  
    path("categories", views.CategoryListAPIView.as_view()),
    path("Food", views.FoodListAPIView.as_view()), 
    path("latest", views.LatestFoodsListAPIView.as_view()),
    path('<slug:category_slug>/<slug:Food_slug>/', views.FoodDetailAPIView.as_view()), 
]
