from django.urls import path
from comments import views

urlpatterns = [
    path('', views.get_comments_by_video_id),
    path('post/', views.post_comment)
]
