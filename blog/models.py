# DATABASE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#database model/class for posts in our blog
class Post(models.Model):
	title = models.CharField(max_length=100) # title with max 100 chars
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now) # data when the object/post is created
	author = models.ForeignKey(User, on_delete=models.CASCADE) # if user deleted, delete the post as well
	likes = models.ManyToManyField(User, related_name='post_like')

	# decides what we want to be printed out in the Django Shell as the results of Post query 
	def __str__(self):
		return self.title

	# returns path to post-detail-route as string, when a post is created	
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def num_of_likes(self):
		return self.likes.count()


