from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teacher_portal.settings")

app = Celery("teacher_portal")

# 👇 Load Django settings (all CELERY_* variables)
app.config_from_object("django.conf:settings", namespace="CELERY")

# 👇 Now override or add custom configs
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")

# Celery Beat schedule
app.conf.beat_schedule = {
    "task_name": {
        "task": "management.tasks.greet",
        "schedule": crontab(minute="*/2"),  # every 2 minutes
    },
}

# Auto discover tasks from all Django apps
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
