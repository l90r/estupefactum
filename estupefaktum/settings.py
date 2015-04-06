"""
Django settings for estupefaktum project. Production environment.
"""

from django.conf import global_settings
from estupefaktum.base_settings import *

import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qw+a7!42e(jz4fpuo7iqkl21rs5oq^*z8owzt=&e6sl$cxx9@$'

DEBUG = True
TEMPLATE_DEBUG = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'estupefaktum.wsgi_production.application'

DATABASES = { 'default': dj_database_url.config() }

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
