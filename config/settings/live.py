import dj_database_url
from django.core.management.utils import get_random_secret_key
from .base import *

# --------------------------------------------------

MIDDLEWARE = [
    'apps.core.middleware.HealthCheckMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'apps.core.middleware.ProjectMinifyHtmlMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'unpoly.contrib.django.UnpolyMiddleware',
    'apps.core.middleware.WwwRedirectMiddleware',
    'apps.auth_user.middleware.TimezoneMiddleware',
]

DEBUG = False

SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

ALLOWED_HOSTS = [
    f'.{ROOT_DOMAIN}',
    "localhost",
]

CSRF_TRUSTED_ORIGINS = [
    f'https://*.{ROOT_DOMAIN}',
]

SESSION_COOKIE_DOMAIN = f'.{ROOT_DOMAIN}'

CSRF_COOKIE_DOMAIN = f'.{ROOT_DOMAIN}'

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

SECURE_REDIRECT_EXEMPT = [r'^wss/$', ]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

# ------------------------------------

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default = os.getenv("DATABASE_URL"),
        conn_max_age = 0,
        conn_health_checks = True,
        ssl_require = True,
    ),
} 

# ------------------------------------

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

ANYMAIL = {
    "MAILGUN_API_KEY": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "MAILGUN_SENDER_DOMAIN": "mg.example.com",
    "MAILGUN_WEBHOOK_SIGNING_KEY": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
}

# ------------------------------------

# Cloudflare R2

AWS_ACCESS_KEY_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AWS_SECRET_ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AWS_STORAGE_BUCKET_NAME = 'bucket-name'
AWS_S3_REGION_NAME = 'auto'
AWS_S3_ENDPOINT_URL = 'https://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.r2.cloudflarestorage.com'
AWS_S3_OBJECT_PARAMETERS = { 'CacheControl': 'max-age=86400' }
AWS_QUERYSTRING_EXPIRE = 36000
AWS_IS_GZIPPED = True
AWS_S3_CUSTOM_DOMAIN = f'cdn.{ROOT_DOMAIN}'

# ------------------------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STORAGES = {
    "default": {
        "BACKEND": "config.storage_backends.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "config.storage_backends.StaticStorage",
    },
}