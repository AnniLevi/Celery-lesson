from django.db import models


class Task(models.Model):
    text = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    success = models.BooleanField(null=True, blank=True)
