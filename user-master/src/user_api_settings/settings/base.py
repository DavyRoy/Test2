import datetime
import os

import dj_database_url
import sentry_sdk
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from sentry_sdk.integrations.django import DjangoIntegration

import environ

env = environ.Env()
environ.Env.read_env()

# env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')  # REQUIRED! FOR COLLECT STATIC
DEBUG = False
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split()
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST').split()
RABBITMQ_URL = env('RABBITMQ_URL')
CSRF_TRUSTED_ORIGINS=['https://genesis-user.2mrw.tech']
KPI_TITLE = env('KPI_TITLE')
KPI_EXCHANGE = env('KPI_EXCHANGE')

KEYDB_HOST = env('KEYDB_HOST')
KEYDB_PORT = env('KEYDB_PORT')
KEYDB_DB = env('KEYDB_DB')
KEYDB_PASSWORD = env('KEYDB_PASSWORD')

DATABASE_URI = env('DATABASE_URI')
SUPERUSER_USERNAME = env('SUPERUSER_USERNAME')
SUPERUSER_PASSWORD = env('SUPERUSER_PASSWORD')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'drf_yasg',

    'user_api.apps.UserApiConfig'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.CacheMiddleware',
]

ROOT_URLCONF = 'user_api_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'user_api_settings.wsgi.application'


# Database

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URI, conn_max_age=600)
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://default:{KEYDB_PASSWORD}@{KEYDB_HOST}:{KEYDB_PORT}',
        'OPTIONS': {
            'db': KEYDB_DB,
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=14),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=21),
    'ROTATE_REFRESH_TOKENS': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'super_secret',
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}


if DEBUG:
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=10000),
        'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=10000),
        'ALGORITHM': 'HS256',
        'SIGNING_KEY': 'super_secret',
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': True,
    }


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

RABBITMQ_URL = 'amqp://user:user@rabbitmq:5672/%2F'
AUTH_USER_MODEL = 'user_api.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
