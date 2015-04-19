"""
Django settings for estupefaktum project. Development environment.
"""

from django.conf import global_settings
from estupefaktum.base_settings import *

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'estupefaktum.wsgi_development.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
