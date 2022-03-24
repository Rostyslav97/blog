from django.urls import path
from core.views import PostListCreateAPI

urlpatterns = [
    path("posts/", PostListCreateAPI.as_view()),
]