import os

CELERY_IMPORTS = ('yt2mp3.tasks',)

BROKER_URL = os.environ['BROKER_URL']

CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_ACCEPT_CONTENT = ['json']
