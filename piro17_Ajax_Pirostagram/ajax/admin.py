from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'content']
  list_display_links = list_display

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['text']