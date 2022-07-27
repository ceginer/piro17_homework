from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def main(request):
  posts = Post.objects.all()
  comments = Comment.objects.all()
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
    form = CommentForm()
    context= {
      'form' : form,
      'comments' : comments,
      'posts' : posts
    }
 
  return render(request, 'ajax/main.html', context=context)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete(request):
  req=json.loads(request.body)
  comment_id=req['id']
  comment_del = Comment.objects.get(id=comment_id)
  comment_del.delete()

  return JsonResponse({'id' : comment_id})

@csrf_exempt
def press_like(request):
    if request.method == 'GET':
        comment_list = Comment.objects.all()
        ctx = {"comments": comment_list}
        return render(request, 'ajax/main.html', ctx)
    elif request.method == 'POST':
        req = json.loads(request.body)
     # load는 파이썬이 이해할 수 있는 형식으로 저장함
        comment_id = req['id']
        comment = Comment.objects.get(id=comment_id)
        if comment.like == True:
            comment.like = False
        elif comment.like == False:
            comment.like = True
        comment.save()
        return JsonResponse({'id': comment_id, 'type': comment.like})


