from django.contrib.auth.forms import AuthenticationForm
from simplemathcaptcha.fields import MathCaptchaField
from django.contrib.auth.models import User

class UserAuthenticationForm(AuthenticationForm):
    captcha = MathCaptchaField()
    class Meta:
        model = User
        fields = ['username','password','captcha']