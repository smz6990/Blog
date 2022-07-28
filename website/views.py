from django.shortcuts import render

# Create your views here.
def website_index(request):
    return render(request,'website/index.html')