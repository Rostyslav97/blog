from re import L
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Post
from core.serializers import PostSerializer

class PostListCreateAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"