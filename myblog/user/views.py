from django.shortcuts import render , redirect
from .form import Register
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = Register()
    return render(request,'user/register.html',{'form':form})

def logout_view(request):
    logout_view(request)
    return render(request,'user/logout.html')