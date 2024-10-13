"""
Django settings for the project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import sys
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Set Apps Directory
APPS_DIR = os.path.join(BASE_DIR, 'apps')

# This allows easy placement of apps within
#  the interior 'apps' directory.
sys.path.append( APPS_DIR )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

WSGI_APPLICATION = 'config.wsgi.application'

ASGI_APPLICATION = 'config.asgi.application'

DATA_UPLOAD_MAX_MEMORY_SIZE = 9372800

ADMINS = [
    ('Naveen Y', 'naveeny.social@gmail.com'),
]

MANAGERS = [
    ('Naveen Y', 'naveeny.social@gmail.com'),
]

# --------------------------------------------

# Custom configs

SITE_NAME = "App Name"
ROOT_DOMAIN = "example.com"
FULL_DOMAIN = f"https://{ROOT_DOMAIN}"

# --------------------------------------------

DEFAULT_EMAIL = f'notifications@{ROOT_DOMAIN}'

DEFAULT_FROM_EMAIL = f'{SITE_NAME} <{DEFAULT_EMAIL}>'

REPLY_TO_EMAIL = f'hello@{ROOT_DOMAIN}'

SERVER_EMAIL = DEFAULT_FROM_EMAIL

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'

LOGOUT_REDIRECT_URL = '/login/'

# Application definition

DJANGO_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sitemaps',
]

PROJECT_APPS = [
    'auth_user',
    'core',
]

PACKAGES = [
    'django_countries',
    'anymail',
    'storages',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'django_htmx',
    'debug_toolbar',
    'django_minify_html',
    'django_browser_reload',
    'django_filters',
    'trix_editor',
    'template_partials',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + PACKAGES

SITE_ID = 1

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# ------------------------------------------------------------------------

AUTH_USER_MODEL = 'auth_user.AuthUser'

AUTHENTICATION_BACKENDS = [
    'apps.auth_user.backends.CustomAuthBackend',
]

# ------------------------------------------------------------------------

INTERNAL_IPS = [ '127.0.0.1', ]

# ------------------------------------------------------------------------

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-dark',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# ------------------------------------------------------------------------

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join( BASE_DIR, 'templates' )],
        "APP_DIRS": True,
        'OPTIONS': {
            # 'loaders': [
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #     ]),
            # ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.context',
            ],
        },
    }
]

# ------------------------------------------------------------------------

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# ------------------------------------------------------------------------

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_TZ = True

TIME_ZONE = 'UTC'

FIRST_DAY_OF_WEEK = 1

USE_THOUSAND_SEPARATOR = True

# -------------------------------------------- 