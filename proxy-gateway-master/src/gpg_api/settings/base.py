import datetime
import os

import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')  # REQUIRED! FOR COLLECT STATIC
DEBUG = env('DEBUG')
DEV_ENV = int(env('DEV_ENV'))
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split()
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST').split()
CORS_ORIGIN_ALLOW_ALL = True
from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
                    "Access-Control-Allow-Origin",
                                ]

RABBITMQ_URL = env('RABBITMQ_URL')

DATABASE_URI = env('DATABASE_URI')

KEYDB_HOST = env('KEYDB_HOST')
KEYDB_PORT = env('KEYDB_PORT')
KEYDB_DB = env('KEYDB_DB')
KEYDB_PASSWORD = env('KEYDB_PASSWORD')

USER_API_URL = env('USER_API_URL')
USER_API_TOKEN = env('USER_API_TOKEN')
USER_API_SALT = env('USER_API_SALT')
USER_API_ALGORITHM = env('USER_API_ALGORITHM')

DOCUMENT_API_URL = env('DOCUMENT_API_URL')
DOCUMENT_API_TOKEN = env('DOCUMENT_API_TOKEN')

TASK_API_URL = env('TASK_API_URL')
TASK_API_TOKEN = env('TASK_API_TOKEN')

SUPERUSER_USERNAME = env('SUPERUSER_USERNAME')
SUPERUSER_PASSWORD = env('SUPERUSER_PASSWORD')

S3_HOST: str = env('S3_HOST')
S3_ACCESS_KEY: str = env('S3_ACCESS_KEY')
S3_SECRET_KEY: str = env('S3_SECRET_KEY')
S3_BUCKET: str = env('S3_BUCKET')
S3_KEY: str = env('S3_KEY')



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

    'gpg.apps.GpgConfig'
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
    'gpg.middleware.ProcessExceptionMiddleware'
]

ROOT_URLCONF = 'gpg_api.urls'

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

WSGI_APPLICATION = 'gpg_api.wsgi.application'


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
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'default_limit': 50,
    'DEFAULT_PERMISSION_CLASSES': (
        'gpg.permissions.IsUserApiAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
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

# if DEBUG:
#     REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = 'rest_framework.permissions.AllowAny'

REST_SESSION_LOGIN = True

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
#     'ALGORITHM': 'RS512',
#
# }


if DEBUG:
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=10000),
        'SIGNING_KEY': 'super_secret',
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': True,
    }


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
