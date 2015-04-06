"""
Django settings for estupefaktum project. Development environment.
"""

from django.conf import global_settings
from estupefaktum.base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qw+a7!42e(jz4fpuo7iqkl21rs5oq^*z8owzt=&e6sl$cxx9@$'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
