from celery import shared_task
import django

django.setup()
from .models import Task


@shared_task
def delete_completed_tasks():
    Task.objects.filter(complete=True).delete()
    return "deleted"
