from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="아이디어명")
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="image")
    content = models.TextField(verbose_name="아이디어 설명")
    interest = models.IntegerField(verbose_name="아이디어 관심도")
    devtool_CHOICES = (
      ('django', 'django'),
      ('react', 'react'),
      ('spring', 'spring'),
      ('node.js', 'node.js'),
      ('java', 'java'),
      ('C++', 'C++'),
  )
    devtool = models.CharField (max_length=7, choices=devtool_CHOICES, verbose_name="예상 개발툴", null = True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Devtool(models.Model):
  name = models.CharField(max_length=50, verbose_name='이름')
  kind = models.CharField(max_length=50, verbose_name='종류')
  content = models.TextField(verbose_name="개발툴 설명")