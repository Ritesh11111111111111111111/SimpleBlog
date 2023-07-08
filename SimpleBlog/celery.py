import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simpleblog.settings")

app = Celery("simpleblog")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()