FROM python:3.7.2-stretch

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD [ "uwsgi", "app.ini" ]
