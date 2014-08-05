import os
import sys

import yt2mp3
import yt2mp3.s3
from .test_yt2mp3 import VALID_URL

KEYNAME = 'test.mp3'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please provide a bucket name."
        sys.exit(1)

    bucketname = sys.argv[1]

    print "downloading and converting to mp3"
    with yt2mp3.download_link(VALID_URL) as filename:
        print "mp3 is at %s" % filename
        print "uploading to s3 bucket '%s'" % bucketname
        yt2mp3.s3.upload_mp3(filename, bucketname, KEYNAME)
        print "uploaded to http://%s.s3.amazonaws.com/%s" % (
            bucketname,
            KEYNAME
        )
