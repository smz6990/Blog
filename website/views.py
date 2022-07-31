from django.shortcuts import render,redirect
from django.urls import reverse
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submited successfully')
            return redirect(reverse('website:contact'))
        else:
            messages.error(request,'Something was wrong')
            messages.error(request,form.errors)
    form = ContactForm()
    context = {'form':form}
    return render(request,'website/contact.html',context)

def newsletter_view(request):
    next = request.POST.get('next','/')
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submited successfully')
            return redirect(next)
        else:
            messages.error(request,'Something was wrong')
            messages.error(request,form.errors)
    return redirect(next)