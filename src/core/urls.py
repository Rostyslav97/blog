from django.urls import path
from core.views import PostListCreateAPI, PostRetrieveUpdateDestroy

urlpatterns = [
    path("", PostListCreateAPI.as_view()),
    path("<int:id>/", PostRetrieveUpdateDestroy.as_view()),
]