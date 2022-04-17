from django.contrib import admin    
from . models import userProfile, Neighborhood

# Register your models here.
admin.site.register(userProfile)
admin.site.register(Neighborhood)