import os
import uuid
import subprocess

AUDIO_EXT = 'mp3'

CMDLINE = [
    'youtube-dl',
    '--extract-audio',
    '--audio-format', AUDIO_EXT,
    '--prefer-avconv',
    '--quiet',
    '--no-playlist'
]

def is_link_valid(url):
    devnull = open('/dev/null', 'w')
    try:
        return subprocess.call(
            CMDLINE + ['-s', url],
            stderr=devnull
        ) == 0
    finally:
        devnull.close()

class download_link(object):
    def __init__(self, url):
        self.url = url
        self.basename = os.path.abspath(str(uuid.uuid4()))
        self.abspath = self.basename + '.' + AUDIO_EXT

    def __enter__(self):
        subprocess.check_call(CMDLINE + [
            '--output', self.basename + r'.%(ext)s',
            self.url
        ])
        return self.abspath

    def __exit__(self, type, value, traceback):
        if os.path.exists(self.abspath):
            os.unlink(self.abspath)
