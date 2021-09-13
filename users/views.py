from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required #decorator

# function for registration form so that new users can sign up
def register(request):
	if request.method == 'POST': # if the request is a POST 
		form = UserRegisterForm(request.POST) # create a form that has POST data
		if form.is_valid():
			form.save() # save user
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!. You can now log in.') #flash msg to show that we have received valid data
			print("SUCCESS")
			return redirect('login') #redirect user to homapage after form is filled

	else:
		form = UserRegisterForm() #create a blank form
	return render(request, 'users/register.html', {'form': form}) # use this template



#user profile
@login_required #login required to view profile
def profile(request):
	if request.method == 'POST': # when POST is done to update user profile with new dat
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		# update profile and save if valid
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated') # flash msg
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {'u_form': u_form, 'p_form': p_form}
	return render(request, 'users/profile.html', context) # use this template