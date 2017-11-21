LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s (%(name)s) %(levelname)s: %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'interval': 24,
            'backupCount': 7,
            'encoding': 'UTF-8',
            'formatter': 'verbose',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/colab/colab.log',
        }
    },
    'loggers': {
        'revproxy': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
        'colab': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
    },
}
