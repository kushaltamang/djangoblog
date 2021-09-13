from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): # inherits from UserCreationForm
	email = forms.EmailField() # get user email

	# keeps configs in one place
	class Meta:
		model = User #create a new user
		fields = ['username', 'email', 'password1', 'password2'] # fields shown in our form, in order

#form to update our user(email, username)
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']

# update profile pic
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']