from django.http import HttpResponse
from bigdeal.tasks import func_task
from bigdeal.models import Task
from django.conf import settings
from datetime import datetime
from pytz import UTC


def func(request):
    value = request.GET.get('value', 0)
    task = Task.objects.create()
    func_task.delay(task.id, value)  # обращение к CELERY_BROKER_URL и передача данных для решения
    return HttpResponse(f'When your task will be completed, you can get the result by id: {task.id}')


def check(request, id):
    task = Task.objects.get(id=id)
    result = ''
    status = 201
    if task.text is not None and task.success:
        result = task.text
        status = 200
    elif (datetime.now(UTC) - task.date_time).seconds > settings.CELERY_TASK_TIME_LIMIT and task.success is None:
        result = 'Task time limit exited'
        status = 500
    elif task.success == False:
        status = 500
    return HttpResponse(result, status=status)
