from mysite.settings import *


DEBUG = False

MAINTENANCE_MODE = False

if MAINTENANCE_MODE:
    MIDDLEWARE.append('mysite.middleware.MaintenanceModeMiddleware')
    
ALLOWED_HOSTS = ['salehmzh.ir','www.salehmzh.ir','127.0.0.1']


with open('mysite/setting/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

ALLOWED_HOSTS.append('example.com')

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True


DATABASES = {
    'default': {
        'NAME': 'djangodatabase',
        'USER': 'dbadmin',
        'PASSWORD': '12345',
        'HOST': 'localhost',
    }
}


DATABASES = {
    'default': {     
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'salehmzh_wizardblog',
        'USER': 'salehmzh_salehwizardsaleh',
        'PASSWORD': '--{_mUts](ME',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# we have to change the BASE_DIR to our public_html file on our site

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]