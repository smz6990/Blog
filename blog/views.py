from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post
# Create your views here.
def blog_index_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts':posts}
    return render(request,'blog/blog-index.html',context)

def blog_single_view(request,pid):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)