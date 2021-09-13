from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# handles traffic from the homepage of our blog
# returns what the user sees when user goes to the homepage
# function-view
def home(request):
	context = {
		'posts': Post.objects.all() # get all the Post data we added using Django Shell
	}

	return render(request, 'blog/home.html', context)

# class-based view for listing posts in the homepage
# paginate this
class PostListView(ListView):
	# model to query in order to create a post
	model = Post
	template_name = 'blog/home.html' # use this template
	context_object_name = 'posts'
	ordering = ['-date']
	paginate_by = 5 # paginate by 5 posts per page

# class-based view for listing posts in the homepage for a particular user 
# paginate this
class UserPostListView(ListView):
	# model to query in order to create a post
	model = Post
	template_name = 'blog/user_posts.html' # use this template
	context_object_name = 'posts'
	paginate_by = 5 # paginate by 5 posts per page

	# get query set for a user
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date') # return all the filtered posts for a user, ordered by latest date

# class-based view for detailed posts view
class PostDetailView(DetailView):
	# model to query 
	model = Post
	
# class-based view to create a new-post
class PostCreateView(LoginRequiredMixin, CreateView): # need to login before creating a post
	# model to query 
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user # set author to current logged in user
		return super().form_valid(form) # validate form by using parent class's func

# class-based view to update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # need to login before creating a post, only author of the post can update that post
	# model to query 
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user # set author to current logged in user
		return super().form_valid(form) # validate form by using parent class's func

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author: # make sure current logged in user = author of post we are trying to update
			return True
		return False

# class-based view for deleting post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	# model to query 
	model = Post
	success_url = '/' # redirect to homepage after the post is deleted

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author: # make sure current logged in user = author of post we are trying to update
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})


