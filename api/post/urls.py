from django.urls import path, include
from rest_framework import routers

from api.post.views.post import PostViewSet

router = routers.SimpleRouter()
router.register(r'post', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
