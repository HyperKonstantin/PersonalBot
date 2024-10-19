FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

ENV PYTHONUNBUFFERED="1"

RUN apt update
RUN apt install -y python3-pip
RUN pip install telebot
RUN pip install selenium
RUN pip install beautifulsoup4
RUN pip install webdriver-manager

CMD ["python3", "main.py"]
