from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		# First we call the parent class's save method
		super().save(*args, **kwargs)
		# Open the image of the current instance
		img = Image.open(self.image.path)

		# Check to see if image is larger than 300 pixels
		if img.height > 300 or img.width > 300:
			# Set max output size
			output_size = (300, 300)
			# Resize image to output size
			img.thumbnail(output_size)
			# Save resized image to same path to overwrite it
			img.save(self.image.path)
