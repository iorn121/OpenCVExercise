FROM python:3.6
USER root

RUN apt-get update -y
RUN apt-get -y install locales
RUN apt-get -y install libopencv-dev 
RUN apt-get clean 
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TX Asia/Tokyo
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install numpy opencv-python matplotlib ffmpeg

WORKDIR /root/opt