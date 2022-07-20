from django.contrib import admin
from .models import Post, Devtool
# Register your models here.

# admin 기본 세팅
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  pass

@admin.register(Devtool)
class DevtoolAdmin(admin.ModelAdmin):
  pass