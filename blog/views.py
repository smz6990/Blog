from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from blog.models import Post,Comment
from blog.forms import CommentForm
from django.contrib import messages

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def index_view(request,**kwargs):
    
    posts = Post.objects.filter(published_date__lte=timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'] )
    
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']] )
    
    posts = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        posts = posts.get_page(page)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    
    context = {'posts':posts}
    return render(request,'blog/blog-index.html',context)


def blog_single_view(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Comment Submited successfully and after approval will be shown in comment section')
        else:
            messages.error(request,'Something went wrong')
            messages.error(request,form.errors)
        return redirect(reverse('blog:single',args=[pid]))

    posts = Post.objects.filter(published_date__lte=timezone.now())
    post = get_object_or_404(posts,pk=pid)
    post.counted_views +=1
    post.save()
    comments = Comment.objects.filter(post=post.id,approved=True)
    form = CommentForm()
    context = {'post':post,'comments':comments,'form':form}
    return render(request,'blog/blog-single.html',context)


def search_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    if request.method == 'GET':
        if Search := request.GET.get('Search'):
            posts = posts.filter(content__contains=Search) 
            posts = Paginator(posts,2)
            page = request.GET.get('page')
            try:
                posts = posts.get_page(page)
            except PageNotAnInteger:
                posts = posts.page(1)
            except EmptyPage:
                posts = posts.page(1)
                    
            context = {'posts':posts}
            return render(request,'blog/blog-index.html',context)
    return render(request,'website/index.html')