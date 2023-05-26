from django.contrib import admin

from .models import Category, Developer, Game

admin.site.register(Category)
admin.site.register(Developer)
admin.site.register(Game)

