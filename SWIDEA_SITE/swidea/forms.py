from django import forms
from .models import Devtool, Post

class PostForm(forms.ModelForm):
    #tool = forms.ModelChoiceField(queryset=Tool.objects.all())
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['image'].required = True
        self.fields['content'].required = True
        self.fields['interest'].required = True
        self.fields['devtool'].required = True
        
        new_choices = []
        tool = Devtool.objects.all()
        for t in tool:
            temp = []
            temp.append(t.name)
            temp.append(t.name)
            temp = tuple(temp)
            new_choices.append(temp)
        new_choices = tuple(new_choices)
        
        self.fields['tool_choice'] = forms.ChoiceField(choices=new_choices, label="예상 개발 툴")
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
