# FROM ubuntu:18.04
# RUN apt-get update && apt-get install -y tesseract-ocr-eng
# RUN apt-get install -y python3 python3-pip

# # Python
# COPY requirements.txt .
# RUN pip3 install --no-cache-dir -r requirements.txt

FROM python:3.7.6-buster
# FROM ubuntu:18.04
RUN apt-get update
# RUN apt-get install -y python3 python3-pip
RUN apt-get install -y tesseract-ocr-eng

# ARG project_dir=/app/

# ADD requirements.txt $project_dir
# ADD reply.py $project_dir

# WORKDIR $project_dir
COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# CMD ["python", "reply.py"]