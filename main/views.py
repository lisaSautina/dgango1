from django.shortcuts import render
from .models import Worker
from .models import Post

def home (request):
    people = Worker.objects.all()
    return render(request, 'main/index.html', {'people': people})

def posts (request):
    dol = Post.objects.all()
    return render(request, 'main/posts.html', {'dol': dol})

