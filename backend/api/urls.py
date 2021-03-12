from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.CommunityView.as_view(), name="Community"),
    path('community/<int:pk>/post/', views.CommunityPostView.as_view(), name="CommunityPost"),
    path('community/<int:community_pk>/post/<int:post_pk>/', views.PostView.as_view(), name="Post"),
    path('post/<int:post_pk>/comment/', views.CommentView.as_view(), name="Comment"),
    path('post/<int:post_pk>/comment/<int:comment_pk>/', views.CommentDetailView.as_view(), name="CommentDelete"),
    path('post/like/<int:pk>/',views.PostLikeView.as_view(), name="PostLike"),
    path('coursepost/',views.CoursePostView.as_view(), name="CoursePost"),
    path('coursepost/<int:pk>/',views.CoursePostDetailView.as_view(), name="CoursePostDetail"),
    path('course/',views.courseView.as_view(), name="Course"),
    path('course/<int:pk>/',views.courseDetailView.as_view(), name="CourseDetail"),
    path('account/',views.accountView.as_view(),name='Account'),
    path('location/',views.location.as_view(),name="Location"),
    path('account/profile/',views.Profile.as_view(),name='Profile'),
    path('recommandcourse/',views.recommandcourse.as_view(),name="RecommandCourse"),
    path('account/mypage/',views.MypageView.as_view(),name="Mypage"),
]