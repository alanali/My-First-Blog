from django.shortcuts import render
from django.utils import timezone
from .models import Post

<<<<<<< HEAD
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
=======
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
>>>>>>> d97cb06337b640a65967d40f5bbdfc195c32ce46
