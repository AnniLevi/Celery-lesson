from celery import shared_task
from bigdeal.models import Task
from time import sleep
from json import dumps


@shared_task
def func(task_id, value):
    task = Task.objects.get(id=task_id)
    task.text = dumps({'result': value ** 5})
    task.save()
    sleep(15)
