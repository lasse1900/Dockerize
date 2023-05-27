FROM python:3.7-alpine

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk add py2-numpy@community py2-scipy@community py-pandas@edge

# RUN apk add --update --no-cache py3-numpy py3-pandas@testing

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
