import os
import unittest

import yt2mp3

VALID_URL = 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
INVALID_URL = 'https://www.youtube.com/watch?v=INVALID'

class TestIsLinkValid(unittest.TestCase):
    def test_returns_true(self):
        self.assertTrue(yt2mp3.is_link_valid(VALID_URL))

    def test_returns_false(self):
        self.assertFalse(yt2mp3.is_link_valid(INVALID_URL))

class TestDownloadLink(unittest.TestCase):
    def test_file_is_deleted_after_leaving_with(self):
        with yt2mp3.download_link(VALID_URL) as filename:
            self.assertTrue(os.path.exists(filename))
        self.assertFalse(os.path.exists(filename))

if __name__ == '__main__':
    unittest.main()
