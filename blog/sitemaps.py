from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from blog.models import Post

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now())

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item):
        return reverse('blog:single',kwargs={'pid':item.id})
