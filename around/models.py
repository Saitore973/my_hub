from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField('image')
    