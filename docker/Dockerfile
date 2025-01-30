FROM debian:trixie-slim
RUN apt-get update -y && apt-get upgrade -y

ARG UID=1000
RUN useradd -ms /bin/bash --uid ${UID} minecraft

RUN apt-get install openjdk-21-jre-headless -y
