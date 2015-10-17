"""
Django settings for cross project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#Use Environment Variable DJANGO_LOCATION to determine location:
#options are: local, staging, and production
DJANGO_LOCATION = os.environ['DJANGO_LOCATION']
 
from cross.secret_keys import DJANGO_KEY, POSTMARK_KEY

SECRET_KEY = DJANGO_KEY

# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_LOCATION == 'local':
    ALLOWED_HOSTS = []

else:
    ALLOWED_HOSTS = ['*']


if DJANGO_LOCATION != 'production':
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = DEBUG

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'refData',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_multiple_model',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    'tags'
)

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)



MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cross.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cross.wsgi.application'

# DJANGO ALLAUTH SETTINGS

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

if DJANGO_LOCATION != 'local':
    SITE_ID = 2
    EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
    POSTMARK_API_KEY = POSTMARK_KEY
    POSTMARK_SENDER = 'info@axiologue.org'
    POSTMARK_TRACK_OPENS = True
else:
    SITE_ID = 3
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_MIN_LENGTH = 6

ACCOUNT_PASSWORD_MIN_LENGTH = 8

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'axiologue_db',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


#Set staticfiles for development
if DJANGO_LOCATION == 'local':
    STATIC_ROOT = '/vagrant/static/'
    MEDIA_ROOT = '/vagrant/media/'
else:
    STATIC_ROOT = '/Axiologue/static/'
    MEDIA_ROOT = '/Axiologue/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'extra_static'),
)

# django-cors-headers configuration
# django-cors-headers configuration
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
#CORS_ORIGIN_WHITELIST = (
#    'api.axiologue.org',
#    'data.axiologue.org'
#)
CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken',
        'access-control-allow-credentials'
    )


# django-debug-toolbar settings
DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1','::ffff:10.0.2.2')

# Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Django allauth settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
LOGIN_REDIRECT_URL = 'http://data.axiologue.org'


if DJANGO_LOCATION =='local':
    #EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'http://localhost:9000/#/login'
else:
    EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
    ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'http://dashboard.floodgaming.com/#/login'


# Python-postmark settings

POSTMARK_API_KEY = POSTMARK_KEY
POSTMARK_SENDER = 'admin@axiologue.org'
DEFAULT_FROM_EMAIL = 'admin@axiologue.org'


