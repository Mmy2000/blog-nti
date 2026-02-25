from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    return render(request , 'home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request,'post_list.html',{"posts":posts})

def post_details(request,id):
    post = Post.objects.get(id=id)
    return render(request , "post_details.html",{"post":post})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request , "post_create.html",{"form":form})

def post_update(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render(request , "post_update.html",{"form":form,"post":post})

def post_delete(request,id):
    post = Post.objects.get(id=id)
    post.delete() 
    return redirect('post_list')