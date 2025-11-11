FROM python:3.9.7-slim-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git curl python3-pip ffmpeg pkg-config libcairo2-dev

RUN pip3 install --upgrade pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

CMD ["bash", "start.sh"]
