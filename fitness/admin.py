from django.contrib import admin
from .models import Weight, Workout

# These are added so that I can edit them in the admin section of django
admin.site.register(Weight)
admin.site.register(Workout)