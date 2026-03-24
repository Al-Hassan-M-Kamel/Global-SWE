
FROM python:3-slim

RUN pip install flask

WORKDIR /app

COPY . /app

EXPOSE 4000

CMD python ./app.py