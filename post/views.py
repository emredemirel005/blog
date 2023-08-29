from django.shortcuts import render
# Create your views here.
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,'index.html',{'posts':posts})

def detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post,}
    return render(request,'detail.html',context)