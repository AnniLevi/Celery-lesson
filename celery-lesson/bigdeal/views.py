from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from bigdeal.tasks import func as func_task
from bigdeal.models import Task


def func(request):
    value = request.GET.get('value', 0)
    task = Task.objects.create()
    func_task.delay(task.id, value)
    return HttpResponse(f'When your task will be completed, you can get the result by id: {task.id}')
