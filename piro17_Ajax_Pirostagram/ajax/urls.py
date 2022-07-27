from django.urls import path
from . import views

app_name = 'ajax'

urlpatterns = [
  # path('',views.main, name='main'),
  path('',views.main,name='main'),
  path('delete/',views.delete,name='delete'),
  path('like/',views.press_like,name='like'),
]