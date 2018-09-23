# Dockerfile for playground ui

FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev build-essential \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install flask \
    && pip3 install requests

ADD playground.py .

EXPOSE 80 5000

ENTRYPOINT ["python3"]

CMD ["playground.py"]
