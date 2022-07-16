from django.db import models
from django.core.validators import *


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 100, verbose_name="제목")
    openyear = models.IntegerField(null = True, verbose_name="개봉 년도", default= '')
    GENRE_CHOICES = (
      ('액션', '액션'),
      ('범죄', '범죄'),
      ('SF', 'SF'),
      ('로맨스', '로맨스'),
      ('코미디', '코미디'),
      ('공포', '공포'),
  )
    genre = models.CharField (max_length=4, choices=GENRE_CHOICES, verbose_name="장르", null = True)
    star = models.FloatField(verbose_name="별점", help_text='value 0 to 5', validators=[MaxValueValidator(5),
            MinValueValidator(0)])
    runningtime = models.CharField(max_length=50, verbose_name="러닝타임")
    moviereview = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=50, verbose_name="감독")
    actor = models.CharField(max_length=50, verbose_name="배우")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)