from socket import fromshare
from django import forms
from .models import Comment

# class PostForm(models.ModelForm):
#   class Meta:
#     model  = Post
#     fields = ('title', 'content',)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('text',)