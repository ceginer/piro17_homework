from django import forms
from .models import Devtool, Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'image','content', 'interest','devtool',)

class PostDev(forms.ModelForm):
  class Meta:
    model = Devtool
    fields = ('name', 'kind','content')



# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ('image')
# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()
