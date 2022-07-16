from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def home(request):

  posts = Post.objects.all()
  context = {"posts": posts}
  return render(request, template_name="reviews/home.html", context=context)


def detail(request, id):

  post= Post.objects.get(id=id)
  context = {
    "post": post
  }
  return render(request, template_name="reviews/detail.html", context=context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'reviews/create.html', {'form': form})

def edit(request, id):
  post = get_object_or_404(Post, id=id)
  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save()
        post.save()
        return redirect(f'/detail/{id}')
  else:
      form = PostForm(instance=post)
  return render(request, 'reviews/create.html', {'form': form})


def delete(request, id):
  post = Post.objects.filter(id=id)
  post.delete()
  return redirect('/')





# def create(request):
#   if request.method == 'POST':
#     # post 요청 값 받기 
#     title = request.POST["title"]
#     openyear = request.POST["openyear"]
#     genre = request.POST["genre"]
#     star = request.POST["star"]
#     runningtime = request.POST["runningtime"]
#     moviereview = request.POST["moviereview"]
#     director = request.POST["director"]
#     actor = request.POST["actor"]

#     # 데이터 베이스에 저장하기 

#     Post.objects.create(title=title, openyear=openyear, genre=genre, star=star, runningtime=runningtime, moviereview=moviereview, director=director, actor=actor)

#     return redirect('/')
#   else:
#     context = {}
#     return render(request, template_name="reviews/create.html", context = context)


