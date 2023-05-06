from django.contrib import admin
from .models import Category, Film, Actor


# Register your models here.
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(Actor)