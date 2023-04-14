from django.urls import path
from .views import CategoryViewser, ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewser, basename='categories')

urlpatterns = router.urls