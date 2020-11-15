FROM python:3.7.6-buster

RUN apt-get update
RUN apt-get install -y tesseract-ocr-eng

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
