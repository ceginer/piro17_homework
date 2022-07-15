from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'reviews'

urlpatterns = [
  path('',views.home, name = "home"),
  path('detail/<int:id>',views.detail, name = "detail"),
  path('create', views.create, name="create"),
  path('edit/<int:id>', views.edit, name= "edit"),
  path('delete/<int:id>',views.delete, name = "delete"),

]