from decouple import config


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': config('DATABASE_HOST', default='127.0.0.1'),
        'NAME': config('DATABASE_NAME', default='colab'),
        'PASSWORD': config('DATABASE_PASSWORD', default=''),
        'USER': config('DATABASE_USER', default='root')
    }
}
