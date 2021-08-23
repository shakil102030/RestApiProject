from .models import Category, Food
from .serializers import CategoryListSerializers, FoodListSerializers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView


class CategoryListAPIView(APIView):
    def get(self, request, fromat=None):
        categories = Category.objects.all()
        serialize = CategoryListSerializers(categories, many=True)
        data = {'categories': serialize.data}
        return Response(data) 



class FoodListAPIView(APIView):
    def get(self, request, fromat=None):
        prod = Food.objects.all()
        serialize = FoodListSerializers(prod, many=True)
        #data = {'categories': serialize.data}
        return Response(serialize.data)

class LatestFoodsListAPIView(APIView):
    def get(self, request, fromat=None):
        Foods = Food.objects.all()[0:4]
        serialize = FoodListSerializers(Foods, many=True)
        return Response(serialize.data) 

class FoodDetailAPIView(APIView):
    def get_object(self, category_slug, Food_slug):
        try:
            return Food.objects.filter(
                category__slug=category_slug).get(slug=Food_slug)
        except Food.DoesNotExist:
            return Http404

    def get(self, request, category_slug, Food_slug, fromat=None):
        Food = self.get_object(category_slug, Food_slug)
        serialize = FoodListSerializers(Food)
        return Response(serialize.data)
    
  
        