from django.contrib.auth.forms import AuthenticationForm
from simplemathcaptcha.fields import MathCaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserAuthenticationForm(AuthenticationForm):
    captcha = MathCaptchaField()
    class Meta:
        model = User
        fields = ['username','password','captcha']
        
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=255,required=False)
    last_name = forms.CharField(max_length=255,required=False)
    captcha = MathCaptchaField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name','captcha']
    
    def save(self,commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if self.cleaned_data['first_name']:
            user.first_name = self.cleaned_data['first_name']
        if self.cleaned_data['last_name']:
            user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user   