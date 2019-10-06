from django.urls import path
from .views import ( PostListView,PostDetailView,PostCreateView,
	PostUpdateView,PostDeleteView,UserPostListView,PostList,home)
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), 
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='blog-about'),
    path('location/', views.loc, name='blog-loc'),
    path('posts/',PostList.as_view(),name='hello')
]



urlpatterns = format_suffix_patterns(urlpatterns)