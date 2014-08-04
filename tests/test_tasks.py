import os
import unittest
import subprocess

os.environ['BROKER_URL'] = 'redis://localhost'
os.environ['CELERY_RESULT_BACKEND'] = 'redis://localhost'

from yt2mp3 import tasks
from .test_yt2mp3 import VALID_URL

worker = None

def setUpModule():
    global worker
    subprocess.check_call(['service', 'redis-server', 'start'])
    worker = subprocess.Popen(['celery', 'worker'])

def tearDownModule():
    global worker
    subprocess.check_call(['service', 'redis-server', 'stop'])
    if worker is not None:
        worker.terminate()
        worker.wait()
        worker = None

class TestTasks(unittest.TestCase):
    def test_convert(self):
        result = tasks.convert.delay(VALID_URL, 'bucket', 'key.mp3')
        result.get(timeout=30)
