import os

from celery import Celery, signals

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject.settings_dev')
app = Celery('demoproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

try:
    from karellen.kombu import register_transports
    register_transports()
except ImportError:
    pass


# See https://github.com/getsentry/raven-python/issues/922
@signals.setup_logging.connect
def setup_logging(**kwargs):
    """Setup logging."""
    pass
