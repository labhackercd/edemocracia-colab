# -*- coding: utf-8 -*-
from decouple import config, Csv


DEBUG = config('DEBUG', cast=bool, default=True)
TEMPLATE_DEBUG = config('TEMPLATE_DEBUG', cast=bool, default=True)

## System admins
ADMINS = [
    (config('ADMIN_USERNAME', default=''), config('ADMIN_EMAIL', default='')),
]

MANAGERS = ADMINS

# general Django settings
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')

# colab-specific
COLAB_FROM_ADDRESS = config('DEFAULT_FROM_EMAIL', default='')
SERVER_EMAIL = config('SERVER_EMAIL', default='')

EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX', default='')

SECRET_KEY = config('SECRET_KEY', default='secret_key')

ALLOWED_HOSTS = config('ALLOWED_HOSTS',
                       cast=Csv(lambda x: x.strip().strip(',').strip()),
                       default='*')

ROBOTS_NOINDEX = config('ROBOTS_NOINDEX', cast=bool, default=True)

## Set URL of Colab home
COLAB_HOME_URL = '/home'

LOGIN_URL = COLAB_HOME_URL

STATIC_ROOT = '/var/labhacker/colab/public/static/'
MEDIA_ROOT = '/var/labhacker/colab/public/media/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', default='')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', default='')

SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY', default='')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET', default='')


LANGUAGE_CODE = 'pt-br'

RIBBON_ENABLED = False

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS