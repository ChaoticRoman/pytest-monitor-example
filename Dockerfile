FROM debian:latest

RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-pytest time \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest-monitor

COPY tests /opt/pytest-monitor-example/tests

WORKDIR /opt/pytest-monitor-example/
