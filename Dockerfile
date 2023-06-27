FROM python:3

WORKDIR /usr/src/app

RUN pip install pytz

ENTRYPOINT [ "python", "main.py" ]
