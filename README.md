This is a [Dockerized][] [Celery][]-based web service that converts
YouTube videos to mp3s.

## Quick Start

```bash
git clone https://github.com/toolness/youtube-to-mp3.git
cd youtube-to-mp3
make image
make develop
```

This will get you into a bash shell in the docker container for the
service. The repository on the docker host is mounted on the docker
container at `/app`.

## Running Tests

You can run all the tests from the docker container with
`python -m unittest discover`.

Individual unit tests can be run with e.g.
`python -m unittest tests.test_yt2mp3`.

  [Dockerized]: http://docker.com/
  [Celery]: http://celeryproject.org/