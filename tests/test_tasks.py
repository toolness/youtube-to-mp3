import os
import unittest
import subprocess

os.environ['BROKER_URL'] = 'redis://localhost'
os.environ['CELERY_RESULT_BACKEND'] = 'redis://localhost'
os.environ['S3_FAKE_UPLOAD_PATH'] = os.curdir

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
    def setUp(self):
        if os.path.exists('bucket_key.mp3'):
            os.unlink('bucket_key.mp3')
    
    tearDown = setUp

    def test_convert(self):
        result = tasks.convert.delay(VALID_URL, 'bucket', 'key.mp3')
        result.get(timeout=30)
        self.assertTrue(os.path.exists('bucket_key.mp3'))
