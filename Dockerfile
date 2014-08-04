FROM ubuntu:14.04
MAINTAINER Atul Varma
RUN printf '\ndeb http://us.archive.ubuntu.com/ubuntu/ trusty multiverse' >> /etc/apt/sources.list
RUN printf '\ndeb http://us.archive.ubuntu.com/ubuntu/ trusty-updates multiverse' >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y libav-tools libavcodec-extra-54 python python-pip python-dev
RUN pip install --upgrade youtube_dl celery[librabbitmq,redis]
