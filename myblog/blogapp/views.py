from django.shortcuts import render , redirect, get_object_or_404
from .models import Blog
from .form import blogform
# Create your views here.

def index(request):
    posts = Blog.objects.all()
    return render(request,'blogapp/index.html',{'posts':posts})

def detail(request,id):
    post = get_object_or_404(Blog, id=id)
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
    
def update(request,id):
    blog = get_object_or_404(Blog, id=id)
    form = blogform(request.POST or None,instance=blog)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blogapp:index')
    return render(request,'blogapp/add-blog.html',{'form':form})

def delete(request,id):
    post = get_object_or_404(Blog, id=id)
    if request.method =='POST':
        post.delete()
        return redirect('blogapp:index')
    return render(request,'blogapp/confirm-delete.html',{'post':post})

def toggle_published(request,id):
    if request.method == 'POST':
        blog =  get_object_or_404(Blog, id=id)
        blog.is_published = not blog.is_published
        blog.save()
        from_page = request.POST.get('from_page','index')
        if from_page == 'detail':
            return redirect('blogapp:detail', id=id)
        else:
            return redirect('blogapp:index')
    return redirect('blogapp:index')