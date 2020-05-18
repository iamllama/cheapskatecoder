from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cheapskatecoder',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    }
}

CORS_ORIGIN_ALLOW_ALL = True