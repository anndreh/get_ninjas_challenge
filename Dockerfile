FROM python:3.5
MAINTAINER Andre Martins "anndreh@gmail.com"
ENV LANG C.UTF-8
ENV TZ America/Sao_Paulo
RUN apt-get update -y
RUN apt-get install libpq-dev build-essential -y
COPY ./app /rover_challenge/app
COPY run.py /rover_challenge
WORKDIR /rover_challenge
CMD ["python", "run.py"]