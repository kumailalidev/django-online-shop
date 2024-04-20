"""
Django development settings
"""

from .base import *
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY",
    default="django-insecure-^uz2g$=t%t)i=3aas2@_ia94q*(&d2m4z7xczlq&@*fn)y*hv6",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",  # Default
        "LOCATION": "",  # Default
    }
}

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS")

# HTTP
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#use-x-forwarded-host
# When USE_X_FORWARDED_HOST is set to True, HttpRequest.build_absolute_uri uses
# the X-Forwarded-Host header instead of request.META['HTTP_HOST'] or
# request.META['SERVER_NAME'].
USE_X_FORWARDED_HOST = True

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# INSTALLED APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    # https://django-extensions.readthedocs.io/en/latest/
    "django_extensions",
    # https://django-debug-toolbar.readthedocs.io/en/latest/
    "debug_toolbar",
]
# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

# MIDDLEWARES
# ------------------------------------------------------------------------------
MIDDLEWARE += [
    # https://django-debug-toolbar.readthedocs.io/en/latest/
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# STRIPE
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = env("STRIPE_API_KEY")
STRIPE_API_VERSION = env("STRIPE_API_VERSION")
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET")

# REDIS
# https://docs.djangoproject.com/en/dev/topics/cache/#redis
REDIS_HOST = "redis"
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_RESULT_BACKEND_DB = 2

# CELERY
# https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULT_BACKEND_DB}"
