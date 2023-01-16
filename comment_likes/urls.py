from django.urls import path
from comment_likes import views


urlpatterns = [
    path('comments/likes/', views.CommentLikeList.as_view()),
    path('comments/likes/<int:pk>', views.CommentLikeDetail.as_view()),
]
