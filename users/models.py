# user profile database model
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) # 1 to 1 relationship(1 user = 1 profile), user delete -> profile delete
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	# how we want profile to be displayed
	def __str__(self):
		return f'{self.user.username} Profile' 

	#override save method of parent class to resize the saved images
	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs) # run save() of parent class
	# 	img = Image.open(self.image.path)

	# 	if img.height > 300 or img.width > 300: #if image > 300 px
	# 		output_size = (300, 300)
	# 		img.thumbnail(output_size) # resize img
	# 		img.save(self.image.path) # save resized img





