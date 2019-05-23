import os
import sys

import raven
from raven.exceptions import InvalidGitRepository

from .base import *

# Do not set SECRET_KEY, Postgres or LDAP password or any other sensitive data here.
# Instead, create a local.py file on the server.

# Disable debug mode
DEBUG = False


# Compress static files offline and minify CSS
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'


# Configuration from environment variables
# Alternatively, you can set these in a local.py file on the server

env = os.environ.copy()

# On Torchbox servers, many environment variables are prefixed with "CFG_"
for key, value in os.environ.items():
    if key.startswith('CFG_'):
        env[key[4:]] = value


# Basic configuration

APP_NAME = env.get('APP_NAME', 'ietf')

if 'SECRET_KEY' in env:
    SECRET_KEY = env['SECRET_KEY']

if 'ALLOWED_HOSTS' in env:
    ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

if 'PRIMARY_HOST' in env:
    BASE_URL = 'http://%s/' % env['PRIMARY_HOST']

if 'SERVER_EMAIL' in env:
    SERVER_EMAIL = env['SERVER_EMAIL']

if 'CACHE_PURGE_URL' in env:
    INSTALLED_APPS += ( 'wagtail.contrib.frontend_cache', )
    WAGTAILFRONTENDCACHE = {
        'default': {
            'BACKEND': 'wagtail.contrib.frontend_cache.backends.HTTPBackend',
            'LOCATION': env['CACHE_PURGE_URL'],
        },
    }

if 'STATIC_URL' in env:
    STATIC_URL = env['STATIC_URL']

if 'STATIC_DIR' in env:
    STATIC_ROOT = env['STATIC_DIR']

if 'MEDIA_URL' in env:
    MEDIA_URL = env['MEDIA_URL']

if 'MEDIA_DIR' in env:
    MEDIA_ROOT = env['MEDIA_DIR']

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.get('PGDATABASE', APP_NAME),
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for

        # User, host and port can be configured by the PGUSER, PGHOST and
        # PGPORT environment variables (these get picked up by libpq).
    }
}


# Redis
# Redis location can either be passed through with REDIS_HOST or REDIS_SOCKET

if 'REDIS_HOST' in env:
    REDIS_LOCATION = env['REDIS_HOST']
    BROKER_URL = 'redis://%s' % env['REDIS_HOST']

elif 'REDIS_SOCKET' in env:
    REDIS_LOCATION = 'unix://%s' % env['REDIS_SOCKET']
    BROKER_URL = 'redis+socket://%s' % env['REDIS_SOCKET']

else:
    REDIS_LOCATION = '127.0.0.1:6379'


if REDIS_LOCATION is not None:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_table',
        },
        'tasks': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': REDIS_LOCATION,
            'KEY_PREFIX': '{}_tasks'.format(APP_NAME),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'ietf': {
            'handlers': ['sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'wagtail': {
            'handlers': ['sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers':     ['mail_admins', 'sentry'],
            'level':        'ERROR',
            'propagate':    False,
        },
        'django.security': {
            'handlers':     ['mail_admins', 'sentry'],
            'level':        'ERROR',
            'propagate':    False,
        },
    },
}


# Log errors to file
if 'ERROR_LOG' in env:
    LOGGING['handlers']['errors_file'] = {
        'level':        'ERROR',
        'class':        'logging.handlers.RotatingFileHandler',
        'filename':     env['ERROR_LOG'],
        'maxBytes':     5242880, # 5MB
        'backupCount':  5
    }
    LOGGING['loggers']['django.request']['handlers'].append('errors_file')
    LOGGING['loggers']['django.security']['handlers'].append('errors_file')


# Sentry
if 'SENTRY_DSN' in env:
    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )

    RAVEN_CONFIG = {
        'dsn': '{}?verify_ssl=0'.format(env['SENTRY_DSN']),
        'tags': {},
    }
    RAVEN_CONFIG['tags']['lang'] = 'python'

    # Prevent logging errors from the django shell.
    # Errors from other management commands will be still logged.
    if len(sys.argv) > 1 and sys.argv[1] in ['shell', 'shell_plus']:
        RAVEN_CONFIG['ignore_exceptions'] = ['*']

    # There's a chooser to toggle between environments at the top right corner on sentry.io
    # Values are typically 'staging' or 'production' but can be set to anything else if needed.
    if 'SENTRY_ENVIRONMENT' in env:
        RAVEN_CONFIG['environment'] = env['SENTRY_ENVIRONMENT']

    # We first assume that the Git repository is present and we can detect the
    # commit hash from it.
    try:
        RAVEN_CONFIG['release'] = raven.fetch_git_sha(BASE_DIR)
    except InvalidGitRepository:
        pass

try:
    from .local import *
except ImportError:
    pass