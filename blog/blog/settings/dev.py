from .base import *   #NOQA


DEBUG = True
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWORD': 'sjdueongh1',
        'HOST': '192.168.255.133',
        'PORT': '3306',
    }
}
