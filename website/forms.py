from django.forms import ModelForm
from website.models import Contact,Newsletter
from simplemathcaptcha.fields import MathCaptchaField

class ContactForm(ModelForm):
    captcha = MathCaptchaField()
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        
class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'