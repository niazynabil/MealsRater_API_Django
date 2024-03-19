from django.contrib import admin
from .models import Meal , Rating
# Register your models here.
admin.site.register(Meal)
admin.site.register(Rating)

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id' , 'meal', 'user' , 'stars']
    list_filter =['meal' , 'user']

class MealAdmin(admin.ModelAdmin):
    list_display=['id' , 'title' , 'description']
    list_filter = ['title' , 'description']
    search_fields = ['title' , 'description']