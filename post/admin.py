from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post, Category, Tags

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tags)
