from django import template
from django.utils import timezone
from blog.models import Category,Post


register = template.Library()

@register.inclusion_tag('blog/blog-categories.html')
def categories_tag():
    posts = Post.objects.filter(published_date__lte=timezone.now())
    categories = Category.objects.all()
    cat_counter = {}
    for name in categories:
        count = posts.filter(category__name=name).count()
        if count>0:
            cat_counter[name]=count
    
    return {'cat_counter':cat_counter}

@register.inclusion_tag('blog/blog-top-stories.html')
def top_stories_tag():
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-counted_views')[:2]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-recent-post.html')
def recent_post_tag():
    post = Post.objects.filter(published_date__lte=timezone.now()).first()
    return {'post':post}