FROM python:3.5.2-slim

MAINTAINER Roman Zhuravskiy <roman.zhuravskiy@gmail.com>

RUN mkdir -p /app && mkdir -p /app/log/
VOLUME ["/app/log"]

RUN groupadd web
RUN useradd -d /home/bottle -m bottle

RUN touch /var/log/bottlesite.all.log
RUN chmod 777 /var/log/bottlesite.all.log

ADD requirements.txt /home/bottle/bottlemock/
ADD server /home/bottle/bottlemock/server/

WORKDIR /home/bottle/bottlemock/server

RUN pip install -r /home/bottle/bottlemock/requirements.txt

EXPOSE 7777
ENTRYPOINT ["/usr/local/bin/python", "/home/bottle/bottlemock/server/app.py"]
USER bottle