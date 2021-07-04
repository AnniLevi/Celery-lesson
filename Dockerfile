FROM python:latest

ADD ./celery-lesson/requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir src
ADD ./celery-lesson src
WORKDIR src
