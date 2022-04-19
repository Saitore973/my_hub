from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

from around.views import neighborhood
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField( 'image',null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} profile'
    
    def __str__(self):
        return self.user.username

class Neighborhood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    image = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    class Meta:
        ordering = ['-created', '-updated']
    
    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
        
    @classmethod
    def search_by_name(cls,search_term):
        neighbours = cls.objects.filter(name__icontains=search_term)
        return neighbours  

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner', blank=True, null=True)

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()