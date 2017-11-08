from decouple import config

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': config('MEMCACHED_LOCATION', default='127.0.0.1'),
    }
}
