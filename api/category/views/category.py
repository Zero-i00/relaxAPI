from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.category.serializers import CategorySerializer
from category.models import Category


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
