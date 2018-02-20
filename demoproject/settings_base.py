from .settings_default import *

CELERY_BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True, 'fanout_patterns': True}

CELERY_RESULT_BACKEND = 'django-db'

INSTALLED_APPS.extend([
    'django_celery_results',
    'django_celery_beat',
])
