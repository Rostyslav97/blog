from django.urls import path
from core.views import PostListCreateAPI, PostRetrieveUpdateDestroyAPI, CommentListCreateAPI, CommentRetrieveUpdateDestroyAPI

urlpatterns = [
    path("posts/", PostListCreateAPI.as_view()),
    path("posts/<int:id>/", PostRetrieveUpdateDestroyAPI.as_view()),
    path("comments/", CommentListCreateAPI.as_view()),
    path("comments/<int:id>/", CommentRetrieveUpdateDestroyAPI.as_view()),
]