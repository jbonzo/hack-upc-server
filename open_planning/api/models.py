from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	avatar = models.ImageField()

class Post(models.Model):
	author = model.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	title = models.CharField(max_length=30)
	description = models.TextField()
	media = models.ImageField()
