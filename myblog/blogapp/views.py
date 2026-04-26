from django.shortcuts import render , redirect
from .models import blog
from .form import blogform
# Create your views here.

def index(request):
    blogs = blog.objects.all()
    return render(request,'blogapp/index.html',{'blogs':blogs})

def detail(request,id):
    post = blog.objects.get(id=id)
    return render(request,'blogapp/detail.html',{'post':post})

def create(request):
    form = blogform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blogapp:index')
    else:
        form = blogform(request.POST or None)
    return render(request,'blogapp/add-blog.html',{'form':form})
    