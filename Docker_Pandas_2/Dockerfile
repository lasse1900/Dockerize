FROM python:3.6-alpine3.7

RUN apk add --no-cache --update \
    python3 python3-dev gcc

RUN pip install --upgrade cython

RUN pip install --upgrade pip 

ADD requirements.txt .
RUN pip install -r requirements.txt
