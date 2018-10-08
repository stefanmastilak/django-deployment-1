from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
	# Create relationship (dont inherit from user!)
	user = models.OneToOneField(User, on_delete=True)
	# add any additional attributes you want
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    # v adresari "media" si vytvorime novy subfolder "profile_pics"
	def __str__(self):
		# built-in attribute of django.contrib.auth.models.User
		return self.user.username
