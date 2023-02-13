import datetime
import os

import dj_database_url
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

import environ


env = environ.Env()
environ.Env.read_env()

# env
RSA_TEST_KEY = env('RSA_TEST_KEY')
RSA_TEST_PUB = env('RSA_TEST_PUB')
DATABASE_URI = env('DATABASE_URI')
SECRET_KEY = env('SECRET_KEY')  # REQUIRED! FOR COLLECT STATIC
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split()
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST').split()
RABBITMQ_URL = env('RABBITMQ_URL')
SUPERUSER_USERNAME = env('SUPERUSER_USERNAME')
SUPERUSER_PASSWORD = env('SUPERUSER_PASSWORD')
# consts

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    'corsheaders',
    'drf_yasg',

    'document.apps.DocumentConfig'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'document_api.urls'

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

WSGI_APPLICATION = 'document_api.wsgi.application'


# Database
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URI, conn_max_age=600)
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
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )}


REST_SESSION_LOGIN = True

SIMPLE_JWT  = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ALGORITHM': 'RS512',
    'SIGNING_KEY': serialization.load_pem_private_key(RSA_TEST_KEY.replace('\\n', '\n').encode('utf-8'), None, default_backend()),
    'VERIFYING_KEY': serialization.load_pem_public_key(RSA_TEST_PUB.replace('\\n', '\n').encode('utf-8'), default_backend()),
}


if DEBUG:
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=10000),
        'SIGNING_KEY': 'super_secret',
    }


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

MEDIA_URL = '/link_documents/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'link_documents')
