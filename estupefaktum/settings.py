"""
Django settings for estupefaktum project. Production environment.
"""

from django.conf import global_settings
from estupefaktum.base_settings import *

import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'estupefaktum.wsgi_production.application'

DATABASES = { 'default': dj_database_url.config() }

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
