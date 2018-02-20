from .settings_base import *

INSTALLED_APPS.extend([
    'raven.contrib.django.raven_compat',
])

RAVEN_CONFIG = {
    'dsn': 'https://...@sentry.io/...',
}

# See https://github.com/getsentry/raven-python/issues/922
CELERYD_HIJACK_ROOT_LOGGER = False

CELERY_BROKER_URL = 'redis://yourdemoaccount.redislabs.com:10217/0'

LOGGING = {
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'sentry'],
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
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
