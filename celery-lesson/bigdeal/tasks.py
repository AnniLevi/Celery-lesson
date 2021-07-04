from celery import shared_task
from bigdeal.models import Task
from time import sleep
from json import dumps


@shared_task  # функция будет запускаться в рамках отдельного процесса, которым будет заниматься celery
def func_task(task_id, value):
    task = Task.objects.get(id=task_id)
    try:
        value = int(value)
        task.text = dumps({'result': value ** 5})
        sleep(10)
        task.success = True
    except Exception as exc:
        task.text = repr(exc)
        task.success = False
    task.save()
