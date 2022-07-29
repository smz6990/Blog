from django.shortcuts import render

# Create your views here.
def website_index_view(request):
    return render(request,'website/index.html')

def website_about_view(request):
    return render(request,'website/about.html')

def website_contact_view(request):
    return render(request,'website/contact.html')