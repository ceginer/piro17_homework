from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Devtool, Post
from .forms import PostForm, PostDev
#  ImageUploadForm

# Create your views here.
def home(request):
  posts = Post.objects.all()
  # 'posts' 는 템플릿에서 사용할 변수 이름
  # posts 는 여기 veiws.py 에서 사용하는 이름
  # context 부분은 항상 딕셔너리 표시
  context = {'posts' : posts}
  return render(request,template_name='swidea/home.html',context=context)

def idea_create(request):
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save()
      post.save()
      return redirect('/')
  else:
    form = PostForm()
  
  return render(request, 'swidea/idea_create.html', {'form' : form})

def idea_detail(request, id):
  post = Post.objects.get(id=id)
  context = {
    'post' : post
  }
  return render (request, template_name="swidea/idea_detail.html", context=context)
  
def idea_update(request, id):
  post = Post.objects.get(id=id)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        post = form.save()
        post.save()
        return redirect(f'/idea_detail/{id}')
  else:
      form = PostForm(instance=post)
  return render(request, 'swidea/idea_update.html', {'form': form})

def delete(request, id):
  post = Post.objects.filter(id=id)
  post.delete()
  return redirect('/')

#######################    devtool   ######################################

def devtool_list(request):
  devtool  = Devtool.objects.all()
  context = {
    'devtools' : devtool
  }
  return render (request, template_name='swidea/devtool_list.html',context=context)

def devtool_create(request):
  if request.method == "POST":
    form = PostDev(request.POST, request.FILES)
    if form.is_valid():
      post = form.save()
      post.save()
      return redirect('/devtool_list')
  else:
    form = PostDev()
  
  return render(request, 'swidea/devtool_create.html', {'form' : form})

def devtool_detail(request, id):
  devtool = Devtool.objects.get(id=id)
  context = {
    'devtool' : devtool
  }
  return render (request, template_name="swidea/devtool_detail.html", context=context)

def detail(request, id):
    idea = Post.objects.get(id=id)
    tools = Devtool.objects.all()
    for tool in tools:
      if tool.name == idea.devtool:
        tool_id = tool.id
    context = {
      "idea":idea,
      "tool_id":tool_id
    }
    return render(request, template_name="swidea/devtool_detail.html",context=context)
  

def devtool_update(request, id):
  devtool = Devtool.objects.get(id=id)
  if request.method == "POST":
    form = PostDev(request.POST, instance=devtool)
    if form.is_valid():
        post = form.save()
        post.save()
        return redirect(f'/devtool_detail/{id}')
  else:
      form = PostDev(instance=devtool)
  return render(request, 'swidea/devtool_update.html', {'form': form})

def devtool_delete(request, id):
  post = Devtool.objects.filter(id=id)
  post.delete()
  return redirect('/devtool_list')