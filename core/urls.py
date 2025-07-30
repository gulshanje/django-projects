# from django.urls import path
# from . import views
# from .views import ItemList

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('api/items/', views.api_items, name='api_items'),
#     path('api/v1/items/', ItemList.as_view()),
# ]

from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CategoryViewSet

router = DefaultRouter()
router.register('items', ItemViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
]
