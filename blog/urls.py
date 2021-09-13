from django.urls import path
from . import views # import views from current directory
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

# when user goes to home path, show views.home
urlpatterns = 	[
				path('', PostListView.as_view() , name='blog-homepage'), # '' is input that represents an empty string, views.home is the function that takes the input
				path('user/<str:username>', UserPostListView.as_view() , name='user-posts'), # template: user_posts.html
				path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # route with integer ID of post as route
				path('post/new/', PostCreateView.as_view(), name='post-create'), # route to create a new post, templaet: <model>/<form>.html
				path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # route with integer ID of post to update a post
				path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # route with integer ID of post to delete a post, template: <model>/<form>.html
			    path('about/', views.about, name='blog-about'), # when user goes to /blog/about, because 'blog' is the homepage
				] 

