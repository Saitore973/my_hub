from django.contrib import admin    
from . models import Profile, Neighborhood, Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Business)
