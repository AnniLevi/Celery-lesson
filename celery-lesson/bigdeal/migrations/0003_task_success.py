# Generated by Django 3.2.5 on 2021-07-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigdeal', '0002_task_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='success',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
