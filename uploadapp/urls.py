from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', FileUploadView.as_view()),
    path('file/', FileView.as_view()),
    path('count/', count_like.as_view()),
    path('like/', LikeView.as_view()),
    path('commentview/', CommentView.as_view()),
    path('comment/', post_comment.as_view())

]