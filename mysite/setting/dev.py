from mysite.settings import *


SECRET_KEY = 'django-insecure-%9+bmn&aa!@&s@$wolzp785o+89xad2oahhg9y(cf+m5^x040p'

DEBUG = True

ALLOWED_HOSTS.append('127.0.0.1')

INSTALLED_APPS.append('debug_toolbar')

# Sites framework settings
SITE_ID = 2

MIDDLEWARE.insert(0,"debug_toolbar.middleware.DebugToolbarMiddleware")

# django debug toolbar settings
INTERNAL_IPS = [
    "127.0.0.1",
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]
