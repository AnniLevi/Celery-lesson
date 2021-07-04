from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from bigdeal.tasks import func_task
from bigdeal.models import Task


def func(request):
    value = int(request.GET.get('value', 0))
    task = Task.objects.create()
    func_task.delay(task.id, value)  # обращение к CELERY_BROKER_URL и передача данных для решения
    return HttpResponse(f'When your task will be completed, you can get the result by id: {task.id}')


def check(request, id):
    task = Task.objects.get(id=id)
    result = ''
    if task.text is not None:
        result = task.text
    return HttpResponse(result)
