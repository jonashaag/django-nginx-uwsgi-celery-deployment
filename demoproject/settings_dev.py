from .settings_base import *

INSTALLED_APPS.extend([
    'karellen.kombu.transport.django',
])

CELERY_BROKER_URL = 'django://'

LOGGING = {
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'celery': {
            'level': 'INFO',
            'propagate': True,
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'version': 1,
    'disable_existing_loggers': False,
}
