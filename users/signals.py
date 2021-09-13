# post save signal for when user is created
from django.db.models.signals import post_save
from django.contrib.auth.models import User # sender of signal 
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #when a user is saved, send a signal to be received by receiver(create_profile function)
def create_profile(sender, instance, created, **kwargs):
	if created: #if user is created
		Profile.objects.create(user=instance) #create a profile for user


@receiver(post_save, sender=User) #when a user is saved, send a signal to be received by receiver(create_profile function)
def save_profile(sender, instance, **kwargs):
	instance.profile.save() #save User