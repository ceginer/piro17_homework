from django.db import models

# Create your models here

class Post(models.Model):
  title = models.CharField(max_length=10, verbose_name='게시글 이름')
  content = models.TextField(verbose_name='게시글 내용')


class Comment(models.Model):
  text = models.CharField(max_length=250, verbose_name='댓글 내용', null=True)
  like = models.BooleanField(default=False, verbose_name='좋아요')
  # post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  # deleted = models.BooleanField(default=False, verbose_name='삭제 여부')