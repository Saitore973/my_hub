from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField( 'image',null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class Neighborhood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    image = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        ordering = ['-created', '-updated']
    
    def __str__(self):
        return self.name
    