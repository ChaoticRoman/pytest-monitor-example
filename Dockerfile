FROM debian:latest

RUN apt-get update \
    && apt-get install -y python3-pip python3-pytest time sqlite3 nano \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest-monitor

COPY tests /opt/pytest-monitor-example/tests
COPY testit /opt/pytest-monitor-example/testit

WORKDIR /opt/pytest-monitor-example/
