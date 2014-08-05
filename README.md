This is a [Dockerized][] [Celery][]-based web service that converts
YouTube videos to mp3s and uploads them to S3.

Since this is partly done as an excuse to learn about Docker and
asynchronous task queues, it is probably bereft of best practices.

## Quick Start

```bash
git clone https://github.com/toolness/youtube-to-mp3.git
cd youtube-to-mp3
make image
cp .env.sample .env
```

Then edit `.env` as needed and run `make run`.

## Calling the Web Service

Just call the `yt2mp3.tasks.convert` task and pass it
the YouTube URL, S3 bucket name, and S3 key id. If the task
returns without throwing an exception, the mp3 will be available
at the bucket and key you specified.

Note that at present, the web service will only accept JSON-serialized
tasks.

## Development

To develop the service, run `make develop`.

This will get you into a bash shell in the docker container for the
service. The repository on the docker host is mounted on the docker
container at `/app`.

## Environment Variables

The following variables must be defined in the container for everything
to work properly.

* `AWS_ACCESS_KEY_ID` is the AWS access key used when uploading to S3.
* `AWS_SECRET_ACCESS_KEY` is the secret access key used when uploading to S3.
* `BROKER_URL` is the Celery [broker URL][] to use.
* `CELERY_RESULT_BACKEND` is the Celery [result backend][] to use.

## Running Tests

You can run all the tests from the docker container with
`python -m unittest discover`.

Individual unit tests can be run with e.g.
`python -m unittest tests.test_yt2mp3`.

These tests use a built-in redis server as their Celery broker and result
backend. They also do not upload to S3.

To test S3 integration, you can run
`python -m tests.manual_test_s3 bucketname`, where *bucketname* is the
name of a bucket to upload a sample `test.mp3` file into.

  [Dockerized]: http://docker.com/
  [Celery]: http://celeryproject.org/
  [broker URL]: http://celery.readthedocs.org/en/latest/configuration.html#broker-url
  [result backend]: http://celery.readthedocs.org/en/latest/configuration.html#celery-result-backend
