FROM ubuntu:22.04
COPY ./janken/ ./usr/python
RUN apt update
RUN apt install -y python3.11 python3-pip
RUN pip3 install pillow