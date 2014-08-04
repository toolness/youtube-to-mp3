from celery import Celery

app = Celery('tasks')

app.config_from_object('celeryconfig')

@app.task
def convert(url, bucker, key):
    import time
    time.sleep(1)
