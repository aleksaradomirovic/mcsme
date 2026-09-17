FROM debian:stable-slim
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    openjdk-21-jre-headless openjdk-25-jre-headless \
    python3 python3-pip \
    python3-platformdirs python3-javaproperties

COPY . /usr/local/src/mcsme
RUN python3 -m pip install -e /usr/local/src/mcsme --break-system-packages --root-user-action=ignore
