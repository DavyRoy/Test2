import datetime
import os

import dj_database_url
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

import environ

env = environ.Env()
environ.Env.read_env()

# env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RSA_TEST_KEY = env('RSA_TEST_KEY')
RSA_TEST_PUB = env('RSA_TEST_PUB')
SECRET_KEY = env('SECRET_KEY')  # REQUIRED! FOR COLLECT STATIC
DEBUG = env('DEBUG')
DEV_ENV = int(env('DEV_ENV'))
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split()
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST').split()
RABBITMQ_URL = env('RABBITMQ_URL')
SUPERUSER_USERNAME = env('SUPERUSER_USERNAME')
SUPERUSER_PASSWORD = env('SUPERUSER_PASSWORD')
DATABASE_URI = env('DATABASE_URI')

KPI_RANGE_DATE = datetime.timedelta(days=14)
KPI_RABBITMQ_TITLE = 'user_kpi'
STATUS_CHANGE_RABBITMQ_TITLE = 'task_status'


CELERY_BROKER_URL = env('CELERY_BROKER_URL')
ARCHIVE_TASK_DELAY_SECONDS = int(env('ARCHIVE_TASK_DELAY_SECONDS'))
ARCHIVE_TASK_DELAY_DAYS = int(env('ARCHIVE_TASK_DELAY_DAYS'))
ARCHIVE_TASK_DELAY = datetime.timedelta(days=ARCHIVE_TASK_DELAY_DAYS, seconds=ARCHIVE_TASK_DELAY_SECONDS)

CELERY_BEAT_SCHEDULE = {
    "test": {
        "task": "gen_task.tasks.archived_tasks",
        "schedule": datetime.timedelta(minutes=5),
    },
}


CELERY_RESULT_BACKEND = 'django-db'

CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 60


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_results',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    'django_filters',

    'gen_task.apps.GenTaskConfig',
    'django_celery_beat',
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
    'middleware.ProcessExceptionMiddleware'
]

ROOT_URLCONF = 'gen_task_api.urls'

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

WSGI_APPLICATION = 'gen_task_api.wsgi.application'


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
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

REST_SESSION_LOGIN = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ALGORITHM': 'RS512',

}

if DEBUG:
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=10000),
        'SIGNING_KEY': 'super_secret',
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': True,
    }

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
