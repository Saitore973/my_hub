from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import  Neighborhood, Profile, Business

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']

class userProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= '__all__'
        exclude = ['user']

class NeighbourhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields= '__all__'
        exclude = ['user']
       

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields= '__all__'
        exclude = ['user', 'neighbourhood']
        
       


