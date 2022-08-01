from django.forms import ModelForm
from blog.models import Comment
from simplemathcaptcha.fields import MathCaptchaField

class CommentForm(ModelForm):
    captcha = MathCaptchaField()
    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']