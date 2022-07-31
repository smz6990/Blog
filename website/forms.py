from django.forms import ModelForm
from website.models import Contact,Newsletter

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        
class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'