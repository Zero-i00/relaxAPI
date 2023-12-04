from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.post.serializers import PostSerializer
from post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
