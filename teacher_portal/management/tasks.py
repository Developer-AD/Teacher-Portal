from celery import shared_task
from django.db.models import Q
from datetime import datetime



@shared_task()
def greet():
    print('*'*100)
    now = datetime.now()
    print(f"Hello - Abhishek: {now}")
    print('*'*100)
    return f'Task-{now}'