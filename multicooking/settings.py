"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from configurations import Configuration, values
import dj_database_url
from django.conf.global_settings import DATABASES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

project = 'multicooking'


class Base(Configuration):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'raven.contrib.django.raven_compat',
        'easy_thumbnails',
        'storages',
        'compressor',
        'shop',
    ]

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'multicooking.urls'

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
                    'django.core.context_processors.media',

                ],
            },
        },
    ]
    WSGI_APPLICATION = 'multicooking.wsgi.application'

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'multicooking',
    #     }
    # }
    RAVEN_CONFIG = {
        'dsn': os.getenv('SENTRY_DSN'),

    }
    ATOMIC_REQUESTS = values.BooleanValue(True)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        #'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #'django.contrib.staticfiles.finders.DefaultStorageFinder',
        'compressor.finders.CompressorFinder',

    ]
    THUMBNAIL_ALIASES = {
        '': {
            'avatar': {'size': (50, 50), 'crop': True},
            'picture': {'size': (800, 500), 'crop': True},
            'large': {'size': (800, 600), 'crop': True},
        },
    }


class Development(Base):
    DEBUG = values.BooleanValue(True)

    STATIC_ROOT = os.path.join(BASE_DIR, 'multicooking/static')
    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'multicooking/media')
    MEDIA_URL = '/media/'


class Production(Base):
    # DEBUG = values.BooleanValue(False)
    # ALLOWED_HOSTS = ['*']
    #
    # AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    # AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    # AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    # AWS_AUTO_CREATE_BUCKET = values.BooleanValue(True)
    # AWS_QUERYSTRING_AUTH = values.BooleanValue(False)
    # AWS = 's3.amazonaws.com'
    # # AWS_CALLING_FORMAT = 2  # SUBDOMAIN
    # # AWS_S3_SECURE_URLS = False
    #
    # DEFAULT_FILE_STORAGE = '%s.s3.Media' % project
    # STATICFILES_STORAGE = '%s.s3.Static' % project
    THUMBNAIL_DEFAULT_STORAGE = '%s.s3.Media' % project
    #
    #
    # MEDIA = 'media'
    # MEDIA_ROOT = MEDIA
    # MEDIA_URL = values.URLValue('https://%s.%s/%s/' % (AWS_STORAGE_BUCKET_NAME, AWS, MEDIA))
    #
    # STATIC = 'static'
    # STATIC_ROOT = STATIC
    # STATIC_URL = values.URLValue('https://%s.%s/%s/' % (AWS_STORAGE_BUCKET_NAME, AWS, STATIC))
    #
    # COMPRESS_ENABLED = True
    # COMPRESS_URL = STATIC_URL
    # COMPRESS_ROOT = STATIC_ROOT
    # COMPRESS_STORAGE = '%s.s3.Static' % project
    # COMPRESS_OFFLINE = False
    #
    DEBUG = values.BooleanValue(False)
    ALLOWED_HOSTS = ['*']

    DATABASES['default'] = dj_database_url.config(conn_max_age=600)

    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_AUTO_CREATE_BUCKET = values.BooleanValue(True)
    AWS_QUERYSTRING_AUTH = False

    COMPRESS_STORAGE = '%s.s3.Static' % project

    DEFAULT_FILE_STORAGE = '%s.s3.Media' % project
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = '%s.s3.CachedS3BotoStorage' % project
    MEDIA_S3 = 'media'
    STATIC_S3 = 'static'
    MEDIA_ROOT = '/%s/' % MEDIA_S3
    STATIC_ROOT = '/%s/' % STATIC_S3
    MEDIA_URL = 'https://%s.s3.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME, MEDIA_S3)
    STATIC_URL = "https://%s.s3.amazonaws.com/%s/" % (AWS_STORAGE_BUCKET_NAME, STATIC_S3)
    COMPRESS_URL = STATIC_URL
