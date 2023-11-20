from django.urls import path

from . import views
from .views import PostUpdateView, PostDetailView, PostCreateView, CategoryListView, PostDeleteView, BlogIndexView, \
    AllCategoriesListView

urlpatterns = [
    path('', BlogIndexView.as_view(), name='blog_index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
    path('category/<category>/', CategoryListView.as_view(), name='blog_category'),
    path('post/create_post/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog_detail'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('categories/', AllCategoriesListView.as_view(), name='all_categories'),
]
