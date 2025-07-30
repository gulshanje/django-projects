from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer, CategorySerializer
from rest_framework import viewsets
from .models import Item, Category

def home(request):
    return render(request, 'core/home.html')

def api_items(request):
    data = list(Item.objects.values())
    return JsonResponse(data, safe=False)

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer