FROM python:3.8-slim

ENV PYTHONBUFFERED 1

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /project

ADD ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT ["sh", "start_service.sh"]