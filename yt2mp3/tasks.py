from celery import Celery
import yt2mp3
import yt2mp3.s3

app = Celery('tasks')

app.config_from_object('celeryconfig')

@app.task
def convert(url, bucket, key):
    with yt2mp3.download_link(url) as filename:
        yt2mp3.s3.upload_mp3(filename, bucket, key)
