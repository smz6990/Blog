from django.shortcuts import render

# Create your views here.
def blog_index_view(request):
    return render(request,'blog/blog-index.html')

def blog_single_view(request):
    return render(request,'blog/blog-single.html')