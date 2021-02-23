FROM ubuntu:20.04
RUN apt-get update && apt-get install -y build-essential && apt-get install -y python3 && apt-get install -y python3-pip && pip3 install pandas
COPY . /home/app/
WORKDIR /home/app/
RUN python3 middleware.py
