import os
import boto
from boto.s3.key import Key

def upload_mp3(filename, bucketname, keyname):
    if 'S3_FAKE_UPLOAD_PATH' in os.environ:
        import shutil
        dst = os.path.join(os.environ['S3_FAKE_UPLOAD_PATH'],
                           bucketname + '_' + keyname)
        return shutil.copyfile(filename, dst)
    if not 'AWS_ACCESS_KEY_ID' in os.environ:
        raise Exception('AWS_ACCESS_KEY_ID env var must be defined')
    if not 'AWS_SECRET_ACCESS_KEY' in os.environ:
        raise Exception('AWS_SECRET_ACCESS_KEY env var must be defined')
    conn = boto.connect_s3()
    bucket = conn.create_bucket(
        bucketname,
        location=boto.s3.connection.Location.DEFAULT
    )
    key = Key(bucket, keyname)
    f = open(filename, 'rb')
    key.set_contents_from_file(f, {'Content-Type': 'audio/mp3'})
    f.close()
    key.make_public()
