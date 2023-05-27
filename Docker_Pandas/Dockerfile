FROM python:3.7-slim-stretch
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./test_pandas.py /
CMD ["python", "/test_pandas.py"]