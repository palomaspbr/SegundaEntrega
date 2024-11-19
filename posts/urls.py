from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_posts, name='index'), 
    path('search/', views.search_posts, name='search'),
    path('create/', views.create_post, name='create'), 
    path('<int:post_id>/', views.detail_post, name='detail'),
    path('update/<int:post_id>/', views.update_post, name='update'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('<int:post_id>/comment/', views.create_comment, name='comment'),
    path('categorys/', views.CategoryListView.as_view(), name='categorys'),
]