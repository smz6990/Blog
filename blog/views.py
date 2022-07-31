from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post,Category
# Create your views here.

def index_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'] )
    context = {'posts':posts}
    return render(request,'blog/blog-index.html',context)


def blog_single_view(request,pid):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def search_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    if request.method == 'GET':
        if Search := request.GET.get('Search'):
            posts = posts.filter(content__contains=Search)
            context = {'posts':posts}
            return render(request,'blog/blog-index.html',context)
        
    return render(request,'website/index.html')