from .base import *
from boto.s3.connection import S3Connection
DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_QUERYSTRING_AUTH = False
# os.environ['S3_USE_SIGV4'] = 'True'
# s3 = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, host='s3.eu-central-1.amazonaws.com')

project = 'multicooking'

DEFAULT_FILE_STORAGE = '%s.s3.Media' % project
STATICFILES_STORAGE = '%s.s3.CachedS3BotoStorage' % project
THUMBNAIL_DEFAULT_STORAGE = '%s.s3.Media' % project
MEDIA = 'media'
MEDIA_ROOT = MEDIA


STATIC = 'static'
STATIC_ROOT = STATIC

COMPRESS_ENABLED = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = '%s.s3.Static' % project
COMPRESS_OFFLINE = False