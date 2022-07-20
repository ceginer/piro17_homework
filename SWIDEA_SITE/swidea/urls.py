from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "swidea"

urlpatterns = [
  path('',views.home, name = "home"),
  path('idea_create',views.idea_create, name = 'idea_create'),
  path('idea_detail/<int:id>',views.idea_detail, name = 'idea_detail'),
  path('idea_update/<int:id>',views.idea_update, name = 'idea_update'),
  path('delete/<int:id>', views.delete, name='delete'),

  path('devtool_list',views.devtool_list,name='devtool_list'),
  path('devtool_detail/<int:id>',views.devtool_detail,name='devtool_detail'),
  path('devtool_create',views.devtool_create,name='devtool_create'),
  path('devtool_delete/<int:id>',views.devtool_delete,name='devtool_delete'),
  path('devtool_update/<int:id>',views.devtool_update,name='devtool_update'),

  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)